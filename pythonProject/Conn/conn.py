from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from urllib.parse import quote_plus

utilisateur = "Deva"
password = "sio"
base_de_donne = "employee"
port = 3306
encoded_password = quote_plus(password)
DB_URL = f'mysql+pymysql://{utilisateur}:{encoded_password}@localhost:{port}/{base_de_donne}'
try:
    ENGINE = create_engine(DB_URL)
    conn = ENGINE.connect()
    print('Votre connexion est OK. L\'objet de connexion est : {} '.format(conn))
except SQLAlchemyError as e:
    print('Erreur SQLAlchemy : {}'.format(str(e)))
except Exception as e:
    print('Erreur inattendue : {}'.format(str(e)))
