from flask import *
from public import public
from admin import admin
from user import user
from blogger import blogger

app=Flask(__name__)

app.secret_key='mos'

app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(user)
app.register_blueprint(blogger)   
       
app.run(debug=True,port=5000,host="0.0.0.0")