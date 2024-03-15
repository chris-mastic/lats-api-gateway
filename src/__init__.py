
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_session import Session
import config
import sys
import os
from dotenv import load_dotenv


# additional_paths = [
#     '/var/www/LATSInternalApi/src',
#     '/var/www/LATSInternalApi/src/db',
#     '/var/www/LATSInternalApi/src/services'
#         ]  
# sys.path.extend(additional_paths)


def create_app():
    load_dotenv()
           
    app = Flask(__name__)
    app.config['SESSION_TYPE']=os.getenv('SESSION_TYPE')
    app.config['SECRET_KEY']=os.getenv('FLASK_SECRET_KEY')
    app.config['DEBUG']=os.getenv('DEBUG')
    app.config['APP_SETTINGS']=os.getenv('APP_SETTINGS')
    app.config['FLASK_APP']=os.getenv('FLASK_APP')
    app.config['FLASK_DEBUG']=os.getenv('FLASK_DEBUG')
    app.config['MONGO_URI'] = 'mongodb://localhost:27017'
    app.config['MONGO_DBNAME'] = 'lats_api_db'
    Session(app)
    cors = CORS(app, resoureces={r"/api/*": {"origins": "http://localhost:19006/"}})
    app.config['CORS_HEADERS'] = 'Content-Type'

    from src.authentication.views import authentication_bp
    from src.change_order.views import change_order_bp


    app.register_blueprint(authentication_bp)
    app.register_blueprint(change_order_bp)

    

    return app

if __name__ == '__main__':
    print("inside if __name__")
    my_app = create_app()
    my_app.run(debug=True)


