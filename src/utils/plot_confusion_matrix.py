import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def plot_confusion_matrix(y_true, y_pred, class_names=None, figsize=(6, 6)):
    """
    Plots the confusion matrix with a heatmap.

    Parameters:
    - y_true: Ground truth labels.
    - y_pred: Predicted labels.
    - class_names: List of class names for the labels. Default is [0, 1].
    - figsize: Size of the heatmap.
    """
    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)

    # Use default class names if none are provided
    if class_names is None:
        class_names = ["Class 0", "Class 1"]

    # Create heatmap
    plt.figure(figsize=figsize)
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=class_names, yticklabels=class_names)
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted Labels")
    plt.ylabel("True Labels")
    plt.show()
