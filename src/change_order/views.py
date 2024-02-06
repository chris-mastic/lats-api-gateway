from flask import Blueprint, request, render_template, jsonify, session, current_app, make_response
import flask
from itsdangerous import URLSafeTimedSerializer
import json
import urllib.request as urlRequest
import urllib.request
import urllib.parse as urlParse
import urllib.error as urlError
import db.oracle_db_connection as odb
import pandas as pd
import services.helpers as helper
import os


change_order_bp = Blueprint("change_order", __name__)


def switch(start: int, stop: int, altid: str, item: str) -> str:
    fips = {"1": "22171", "2": "22172", "3": "22173",
            "4": "22174", "5": "22175", "6": "22176", "7": '22177'}

    val = altid[start:stop]

    if item == 'fips':
        return fips[altid[start:stop]]
    elif item == "ward":
        return '22172'
    elif val == "3":
        return '22173'
    elif val == "4":
        return '22174'
    elif val == "5":
        return '22175'
    elif val == "6":
        return '22176'
    elif val == "7":
        return '22177'
    else:
        return "Invalid altid"


@change_order_bp.route("/api/add_to_batch", methods=['GET', 'POST'])
def add_to_batch():
    """
    You will need to figure out how to add in the token here

    headers = {'accept': '*/*',
               "Content-Type": "application/json",
               "Authorization: Bearer " <token>
               }

    """

    return "ok"


@change_order_bp.route("/api/get_batch", methods=['GET', 'POST'])
def get_batch():
    req = json.loads(request.data)
    parid = req['parid']
    taxyear = req['taxyear']
    # --------------------------------DEBUG---------------
    # print("DEBUG------------------------------------------------------")
    # print(f'flask.session["token"]{flask.session["token"]}')
    # print(f'request.cookies.get("ltcToken"){request.cookies.get("ltcToken")}')
    # print(f'session.sid{session.sid}')
    # print(f'request.cookies.get("session"){request.cookies.get("session")}')

    if helper.is_valid_session(request.cookies.get("session"), session.sid):
        # OracleDB is a singleton class
        try:
            db = odb.OracleDBConnection.getInstance()

            curr_dir = os.path.dirname(__file__)
            print(f'curr_dir {curr_dir}')
            parent_dir = os.path.dirname(curr_dir)
            db_dir = os.path.join(parent_dir, 'db', 'db_scripts')
            sql_filename = os.path.join(db_dir, 'get_batch.sql')

            with open(sql_filename, 'r') as file:
                query = file.read()

            df = pd.read_sql_query(query, db.engine, params=[
                                   (parid, taxyear, 'Y')])

            for ind in df.index:
                parid = df["parid"][ind]
                taxyr = df["taxyr"][ind]
               # fips_code = switch(1,1,df["altid"][ind], 'fips')
                owner = df["own1"][ind]

            data = {'tax_year': str(taxyr),
                    'fips_code': 'fips_code',
                    'assessment_no': "",
                    'ward': "",
                    'assessor_ref_no': "",
                    'place_fips': "",
                    'parcel_address': "",
                    'assessment_type': "",
                    'assessment_status': "",
                    'homestead_exempt': "",
                    'homestead_percent': "",
                    'restoration_tax_expmt': "",
                    'taxpayer_name': owner,
                    'contact_name': "",
                    'taxypayer_addr1': "",
                    'taxypayer_addr2': "",
                    'taxypayer_addr3': "",
                    'tc_fee_pd': "",
                    'reason': "",
                    'check_no': "",
                    'check_amount': "",
                    'assessVaues': [{
                        'ltc_sub_class_old': "",
                        'ltc_sub_class_new': "",
                        'quantity_old': "",
                        'quantity_new': "",
                        'units_old': "",
                        'units_new': "",
                        'other_exempt_old': "",
                        'other_exempt_new': "",
                        'value_old_total': "",
                        'value_new_total': "",
                        'value_old_hs': "",
                        'value_new_hs': "",
                        'value_old_tp': "",
                        'value_new_tp': ""
                    }]
                    }

            json_data = json.dumps(data, default=str)
            return json_data
            # return jsonify({'status': 'extited'})
        except:
            return jsonify({'message': 'Database error'})
    else:
        response = jsonify({
            'message': 'Not logged in'
        })
        helper.clear_session(response)
        return response


@change_order_bp.route("/api/get_status", methods=['GET'])
def get_status():

    req = json.loads(request.data)
    change_order_batch_id = req['changeOrderBatchId']
    tax_year = req['taxYear']
    fips_code = req['fipsCode']

    # Verify user is authenticate
    session_id_from_cookie = request.cookies.get('session')
    print(f'session_id from cookie: {session_id_from_cookie}')
    session_id_from_server = session.sid
    print(f'session id from server {session_id_from_server}')
    # Compare the two IDs
    if session_id_from_cookie == session_id_from_server:
        url = os.environ.get('LTC_API_URL_PROD')
        paths = [url, "Auth/v1/authenticate?param=value&param2=value"]

        url = "".join(paths)
        url = 'https://testapi.latax.la.gov/api/Auth/v1/ChangeOrderGetStatus?param=value&param2=value&param3=value&param4=value'

        values = {"changeOrderBatchId": change_order_batch_id,
                  "taxYear": tax_year,
                  "fipsCode": fips_code
                  }
        headers = {'accept': 'text/plain',
                   "Content-Type": "application/json"}  # ,
        # "Authorization": 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDYxMjQ1MDcsImlzcyI6Imh0dHBzOi8vdGVzdGFwaS5sYXRheC5sYS5nb3YvIiwiYXVkIjoidGVzdCJ9.kz8fdH5-fD03OOW2GCLipNFf-HRQVHS178_3Pd1tgPc'
        # }

        creds = json.dumps(values).encode('utf-8')
        print('after creds')
        req = urllib.request.Request(
            url, headers=headers, data=creds, method='GET')
        print(f"req {req}")
        try:
            print('entering context manager')
            with urlRequest.urlopen(req) as response:
                print('after with, before body')
                body = response.read()
                print('inside with')
            resp = json.loads(body)

            print(f"resp: {resp}")
            # store in the session dictionary
            token = resp['token']
            flask.session["token"] = token
            flask.session['secretkey'] = current_app.secret_key.encode('utf-8')
            flask.session['username'] = resp['userName']
            flask.session['expiration'] = resp['expiration']
            flask.session['roles'] = resp['roles']
            flask.session['userId'] = resp['userId']

            print('before jsonify')
            return jsonify({
                'token': resp['token'],
                'expiration': resp['expiration'],
                'userName': resp['userName'],
                'userId': resp['userId'],
                'roles': resp['roles']
            })

        except urlError.URLError as e:
            message = e.reason
            error_code = e.errno
            return jsonify({'error': error_code,
                            'message': message})

    else:

        return jsonify({'error': 401,
                        'message': 'You are not logged in.'})

    return "ok"
