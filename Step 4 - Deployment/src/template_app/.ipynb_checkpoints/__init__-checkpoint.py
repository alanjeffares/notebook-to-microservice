from flask import Flask
from .main.train import train
from .main.predict import predict
from .main.visualise import visualise


app = Flask(__name__)

app.register_blueprint(predict, url_prefix='/predict')
app.register_blueprint(train, url_prefix='/train')
app.register_blueprint(visualise, url_prefix='/visualise')
