# Walkthrough of Project

1. Create a `load_data` function that reads the csv file stored in data folder.
2. Next we do some pre-processing on the dataset, like dropping unnecessary columns, convert into categorical data, and finally split the data into testing and training set. (70% training, 30% testing.)
3. We will also create a model file, which has 3 options. A model will be selected based on the value passed through the config.json file.
4. Next we will train the model in the train.py file. We will also make predictions and calculate the accuracy score and confusion matrix.
5. Finally we have metrics.py file, which will be printing some import data for analysis of the model.
6. Everything will be called from a central file called main.py. We will also have a test folder consisting of unit_test.py to perform unit testing.
