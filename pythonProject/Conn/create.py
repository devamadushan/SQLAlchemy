from conn import ENGINE, cursor
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker
metadata = MetaData()

user_table = Table(
    'user', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('nom', String(255), nullable=False),
    Column('age', Integer)
)
# Création de la table dans la base de données
metadata.create_all(ENGINE)
Session = sessionmaker(bind=ENGINE)
session = Session()

# Création d'objets "user" et ajout à la base de données
users_data = [
    {'nom': 'Alice', 'age': 25},
    {'nom': 'Bob', 'age': 30},
    {'nom': 'Charlie', 'age': 22}
]

for user_data in users_data:
    user = user_table.insert().values(user_data)
    session.execute(user)

# Validation des changements dans la base de données
session.commit()

