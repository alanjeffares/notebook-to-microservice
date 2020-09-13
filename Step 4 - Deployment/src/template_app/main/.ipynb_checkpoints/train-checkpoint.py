from flask import Blueprint, request
import json
from src.main.train import main

train = Blueprint('train', __name__)


@train.route("/", methods=['GET'])
def train_model():
    """Train model according to current configurations."""
    main()
    return "Training complete"
