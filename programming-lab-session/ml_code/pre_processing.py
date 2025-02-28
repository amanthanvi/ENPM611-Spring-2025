# || START LECTURE NOTES ||
# This is where most of our pre-processing code will be written
# We will be dropping unnecessary columns, converting into categorical values, splitting the data, etc.
# Once we have done everything in pre-processing, we will send it to train.py
# || END LECTURE NOTES ||

# Used to split the data into training and testing sets
from sklearn.model_selection import train_test_split
# Used to convert categorical values into numerical values
from sklearn.preprocessing import LabelEncoder


def preprocess_data(data):
    """
    Preprocess the data by scaling the features and splitting it into training and testing sets.
    """
    # Drop unnecessary columns
    data.drop(columns=['EmployeeCount', 'EmployeeNumber',
                       'Over18', 'StandardHours'], axis="columns", inplace=True)  # Using inplace=True to modify the original dataframe

    categorical_columns = []  # List of categorical columns
    for column in data.columns:  # Iterate through each column
        # Check if the column is categorical and has less than 50 unique values
        if data[column].dtype == object and len(data[column].unique()) <= 50:
            categorical_columns.append(column)  # Add the column to the list

    # Here the Attribution column is is being converted to a categorical data type using .astype('category')
    # .cat.codes is used to convert the categorical values into numerical values
    data['Attrition'] = data.Attrition.astype('category').cat.codes

    # Remove the Attribution column from the list of categorical columns
    categorical_columns.remove('Attrition')

    label = LabelEncoder()  # Create a LabelEncoder object
    for column in categorical_columns:  # Iterate through each categorical column
        # Convert the categorical values into numerical values
        data[column] = label.fit_transform(data[column])

    print(data.head())  # Print the first 5 rows of the data

    # We are going to drop the target variable "Attrition" from the data leaving only input features
    X = data.drop("Attrition", axis=1)
    y = data.Attrition  # Target variable

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42)

    return X_train, X_test, y_train, y_test
