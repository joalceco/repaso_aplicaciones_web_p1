from flask import Flask

app=Flask(__name__)
app.config["SECRET_KEY"]="dsakfasd09asmd9fm"

from app import routes