
def print_unique_values(col_names, df, return_dict=False):
    """
    Prints the unique values for each given column name and optionally returns them as a dictionary.

    :param col_names: List of column names
    :param df: pandas.DataFrame
    :param return_dict: bool, default=False. If True, returns a dictionary of unique values.
    :return: dict (optional)
    """
    unique_values_dict = {}

    for col in col_names:
        if col in df.columns:
            unique_vals = df[col].unique()
            unique_values_dict[col] = unique_vals

            print(f"Unique values in '{col}':")
            print(unique_vals)
            print("\n")
        else:
            print(f"Column '{col}' not found in DataFrame.\n")

    if return_dict:
        return unique_values_dict
