## Step 1 - Refactoring, code style and testing

This is code corresponding to step 1 in my article [Jupyter Notebook to Microservice](link). This code has three main functionalities:
* Train - Trains an `sklearn` pipeline on the iris dataset and saves the best model from a parameter gridsearch evaluated on stratified test data.
* Predict - Loads the latest model and predicts the class of a user input observation.
* Visualise - Produces a pairplot of the iris dataset.

### Project structure
```
├── models       # storage of trained models.
├── src
│   ├── main     # main logic for training, predicting and visualisation.
│   └── utils    # helper functions.
├── tests        # contains projects testing suite. 
├── Readme.md
└── run.py       # entry point of the project for local usage.

```

### Testing 
To run unit tests and pycodestyle, from the root directory run:

    $ sh tests/test_all.sh

To run an individual test script:

    $ python3 tests/unit/test_data_utils.py

### Usage
To run any of the three main functionalities, navigate to the root folder and run the following commands.
To train a new model on the iris data:

    $ python3 run.py train
    
To use the latest model to predict the class of observation `[5.1, 3.8, 1.5, 0.3]`:

    $ python3 run.py predict [5.1, 3.8, 1.5, 0.3]
    
To produce a pairplot of the iris dataset:

    $ python3 run.py visualise
    