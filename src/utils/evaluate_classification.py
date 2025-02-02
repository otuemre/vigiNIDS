from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate_classification(y_true, y_pred, model_name):
    """
    Evaluates the model using various classification metrics.

    Parameters:
    - y_true: Ground truth labels.
    - y_pred: Predicted labels.

    Returns:
    - metrics: A dictionary containing model name, accuracy, precision, recall, and F1-score.
    """
    metrics = {
        "Model Name": model_name,
        "Accuracy": accuracy_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred),
        "Recall": recall_score(y_true, y_pred),
        "F1 Score": f1_score(y_true, y_pred),
    }

    return metrics
