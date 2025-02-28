# || START LECTURE NOTES ||
# Receives pre-processed data from pre_processing.py
# In here, we will be training the model that we have chosen
# In config.json, we will be passing a model a value that will be taken into model.py and that model will be used to train using the dataset
# Once we have everything trained, we will head over to metrics.py
# || END LECTURE NOTES ||

from sklearn.metrics import accuracy_score, confusion_matrix


def train_and_evaluate(model, X_train, X_test, y_train, y_test):
    """
    Train the model and evaluate its performance.
    """
    model.fit(X_train, y_train)  # Train the model
    # Predict the target variable for the test set
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)  # Calculate accuracy
    cm = confusion_matrix(y_test, predictions)  # Calculate confusion matrix

    # Check if the model has a predict_proba method
    if hasattr(model, "predict_proba"):
        # Predict the probabilities of the target variable for the test set
        y_prob = model.predict_proba(X_test)[:, 1]
    else:
        y_prob = None

    return accuracy, cm, y_test, y_prob
