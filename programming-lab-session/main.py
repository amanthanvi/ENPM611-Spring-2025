from ml_code.data_load import load_data
from ml_code.pre_processing import preprocess_data
from ml_code.models import ModelFactory
from ml_code.train import train_and_evaluate
from ml_code.metrics import print_metrics

# First, open the config.json file and load it into a variable called config using json.load()
import json
with open('config.json') as config_file:
    config = json.load(config_file)

# Step 1: Load Data
# Use the relative path 'data/data.json' to load the data into a variable called data

data = load_data("data/data.csv")
print(data.head())  # Print the first 5 rows of the data

# Step 2: Preprocess Data
X_train, X_test, y_train, y_test = preprocess_data(data)

# Step 3: Get the Model from ModelFactory
model = ModelFactory.get_model(config["model_type"])

# Step 4: Train and Evaluate the Model
accuracy, cm, y_test, y_prob = train_and_evaluate(
    model, X_train, X_test, y_train, y_test)

# Step 5: Print Metrics
print_metrics(accuracy, cm, y_test, y_prob)  # cm is confusion matrix
