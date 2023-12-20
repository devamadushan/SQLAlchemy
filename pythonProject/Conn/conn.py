from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from urllib.parse import quote_plus

'''
-pip install sqlalchemy
'''

'''
create database employee;

use employee;


I create a table customers  : 
CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    customer_age INT
);

and i have this kind of objects : INSERT INTO customers (customer_name, customer_age) VALUES
('Alice', 25),
('Bob', 30),
('Charlie', 22),
('David', 40),
('Eva', 35),
('Frank', 28),
('Grace', 50),
('Hank', 45),
('Ivy', 21),
('Jack', 55);
'''

utilisateur = "Deva"
password = "sio"
base_de_donne = "employee"
port = 3306
encoded_password = quote_plus(password)
DB_URL = f'mysql+pymysql://{utilisateur}:{encoded_password}@localhost:{port}/{base_de_donne}'

ENGINE = create_engine(DB_URL)
cursor = ENGINE.connect()

