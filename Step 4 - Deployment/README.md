## Step 4 - Deployment

This is code corresponding to step 4 in my article [Jupyter Notebook to Microservice](link). This code has three main functionalities:
* Train - Trains an `sklearn` pipeline on the iris dataset and saves the best model from a parameter gridsearch evaluated on stratified test data.
* Predict - Loads the latest model and predicts the class of a user input observation.
* Visualise - Produces a pairplot of the iris dataset.

### Project structure
```
├── src
│   ├── conf           # stores project configurations is json format.
│   ├── main           # main logic for training, predicting and visualisation.
│   ├── resources      # storage of resources such as trained models.
│   ├── template_app   # contains all logic for the flask application.
│   └── utils          # helper functions.
├── tests              # contains projects testing suite. 
├── docker-compose.yml # Docker configurations.
├── Dockerfile         # machine instructions to setup the application and run inside Docker as a micro-service.
├── logs.log           # log files storage.
├── Readme.md
├── requirements.txt   # Python dependancies for installation with pip.
├── run_app.py         # entry point of the project for the Flask application.
└── run.py             # entry point of the project for local usage.

```

### Testing 
To run unit tests and pycodestyle, from the root directory run:

    $ sh tests/test_all.sh

To run an individual test script:

    $ python3 tests/unit/test_data_utils.py

### Local usage
To run any of the three main functionalities, navigate to the root folder and run the following commands.
To train a new model on the iris data:

    $ python3 run.py train
    
To use the latest model to predict the class of observation `[5.1, 3.8, 1.5, 0.3]`:

    $ python3 run.py predict [5.1, 3.8, 1.5, 0.3]
    
To produce a pairplot of the iris dataset:

    $ python3 run.py visualise
    
### Starting the Dockerised Flask container
To build the image, ensure docker is installed and run:

    $ docker build <app name>:<app version> .
    
Then to run the image, run:
    
    $ docker run -p 5000:5000 <app name>:<app version>
    
### Running the Flask application
To run the Flask application, from the root directory run:

    $ python3 run_app.py
    
Once the application is running, the following API options are available:
    
- GET `http://localhost:5000/train/`
    
- POST `http://localhost:5000/predict/`
    
- GET `http://localhost:5000/visualise/`
    