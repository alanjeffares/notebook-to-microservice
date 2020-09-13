from flask import Blueprint, request
import json
from src.main.predict import main

predict = Blueprint('predict', __name__)


@predict.route("/", methods=['POST'])
def make_prediction():
    """Make a prediction on a user input value."""
    value = json.loads(request.data)
    prediction = main(value=value)
    return prediction
