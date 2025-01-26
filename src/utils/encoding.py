import pandas as pd

def ordinal_encode(df, col_name, mapping):
    """
    Apply ordinal encoding to a specific column.

    :param df: pandas.DataFrame
    :param col_name: str, column name to encode
    :param mapping: dict, mapping of categories to integers
    :return: pandas.DataFrame with encoded column
    """
    df[col_name] = df[col_name].map(mapping)
    return df

def one_hot_encode(df, col_names):
    """
    Apply one-hot encoding to specific columns.

    :param df: pandas.DataFrame
    :param col_names: list of column names to encode
    :return: pandas.DataFrame with one-hot encoded columns
    """
    return pd.get_dummies(df, columns=col_names, drop_first=True)
