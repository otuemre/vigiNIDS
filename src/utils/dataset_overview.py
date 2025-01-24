import pandas as pd


def load_dataset(file_path):
    """
    Loads a dataset and returns it as a pandas DataFrame.

    Parameters:
    file_path (str): Path to the dataset file.

    Returns:
    pd.DataFrame: Loaded dataset.
    """
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None


def get_dataset_info(df, name):
    """
    Prints basic information about a dataset.

    Parameters:
    df (pd.DataFrame): The dataset to inspect.
    name (str): A descriptive name for the dataset.
    """
    if df is not None:
        print(f"\n{name} Columns:\n{list(df.columns)}")
        print(f"{name} Shape (Rows, Columns): {df.shape}")
    else:
        print(f"\n{name}: Failed to load.")


def inspect_datasets():
    """
    Inspects all datasets related to UNSW-NB15.
    """
    # Dataset file paths
    datasets = {
        "Train Dataset": "src/datasets/UNSW_NB15_training-set.csv",
        "Test Dataset": "src/datasets/UNSW_NB15_testing-set.csv",
        "Ground Truth Dataset": "src/datasets/NUSW-NB15_GT.csv",
    }

    # Full dataset parts
    full_dataset_parts = [
        "src/datasets/UNSW-NB15_1.csv",
        "src/datasets/UNSW-NB15_2.csv",
        "src/datasets/UNSW-NB15_3.csv",
        "src/datasets/UNSW-NB15_4.csv",
    ]

    # Inspect pre-split datasets
    print("Pre-Split Datasets:\n")
    for name, path in datasets.items():
        df = load_dataset(path)
        get_dataset_info(df, name)

    # Inspect full dataset parts
    print("\nFull Dataset Parts:\n")
    total_rows = 0
    for i, path in enumerate(full_dataset_parts, start=1):
        df = load_dataset(path)
        if df is not None:
            total_rows += len(df)
            print(f"Full Dataset Part {i} Shape: {df.shape}")

    print(f"\nTotal Rows in Full Dataset (Combined): {total_rows}")


if __name__ == "__main__":
    inspect_datasets()
