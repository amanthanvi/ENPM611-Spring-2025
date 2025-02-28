from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


class ModelFactory:
    """
    Factory class for creating machine learning models.
    """
    @staticmethod   # This decorator indicates that this method is a static method and does not require an instance of the class to be called.
    def get_model(model_type: str):
        """
        Returns a machine learning model based on the specified type.

        Parameters:
            model_type (str): The type of model to create. Supported types are 'logistic_regression', 'decision_tree', and 'random_forest'.

        Returns:
            model: An instance of the specified machine learning model.
        """
        if model_type == "logistic_regression":
            return LogisticRegression(max_iter=500)
        elif model_type == "decision_tree":
            return DecisionTreeClassifier()
        elif model_type == "random_forest":
            return RandomForestClassifier()
        else:
            raise ValueError(f"Model type '{model_type}' is not supported.")
