from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
import cloudinary
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'HJGGHD*^&R$YGFGHDYTRER&*TRTYCHG^R&^T'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote("Admin@123")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 8

db = SQLAlchemy(app)

cloudinary.config(cloud_name='dxxwcby8l',
                  api_key='448651448423589',
                  api_secret='ftGud0r1TTqp0CGp5tjwNmkAm-A')

login = LoginManager(app)
