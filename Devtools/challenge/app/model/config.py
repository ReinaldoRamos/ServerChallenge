from flask import Flask
import os
app = Flask(__name__,static_folder='../static', template_folder='../templates')

#VARS
db_user = os.getenv("MYSQL_USER")
db_pass = os.getenv("MYSQL_PASSWORD")
db_endpoint = os.getenv("MYSQL_HOST")
db_name = os.getenv("MYSQL_DATABASE")

# #Conection MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_user}:{db_pass}@{db_endpoint}/{db_name}'

# VARS LOCAL
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
