import pandas as pd

def get_numerical_df(df, numerical_features):
    """
    Creates a DataFrame containing only numerical features.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        numerical_features (list): List of numerical feature names.
    
    Returns:
        pd.DataFrame: DataFrame containing only numerical features.
    """
    # Filter the DataFrame to include only specified numerical features
    numerical_df = df[numerical_features].copy()
    
    return numerical_df