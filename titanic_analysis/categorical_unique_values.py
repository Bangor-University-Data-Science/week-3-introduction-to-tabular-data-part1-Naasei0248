import pandas as pd

def display_unique_values(df, categorical_features):
    """
    Displays unique values for each categorical feature in the DataFrame.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        categorical_features (list): List of categorical feature names.
    
    Returns:
        dict: A dictionary where keys are feature names and values are the unique values.
    """
    unique_values_dict = {}
    
    for feature in categorical_features:
        if feature in df.columns:
            unique_values = df[feature].unique()
            unique_values_dict[feature] = unique_values.tolist()
        else:
            unique_values_dict[feature] = f"Feature '{feature}' not found in DataFrame."
    
    return unique_values_dict
