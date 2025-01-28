from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt

def plot_auc_roc(y_true, y_proba):
    """
    Calculates AUC-ROC and plots the ROC curve.

    Parameters:
    - y_true: Ground truth labels.
    - y_proba: Predicted probabilities for the positive class.

    Returns:
    - auc: The computed AUC score.
    """
    auc = roc_auc_score(y_true, y_proba)
    fpr, tpr, thresholds = roc_curve(y_true, y_proba)

    # Plot ROC curve
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color="blue", label=f"AUC = {auc:.2f}")
    plt.plot([0, 1], [0, 1], color="gray", linestyle="--")
    plt.title("ROC Curve")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend(loc="lower right")
    plt.grid()
    plt.show()

    return auc
