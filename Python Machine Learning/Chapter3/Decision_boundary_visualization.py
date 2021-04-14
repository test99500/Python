from matplotlib.colors import ListedColormap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_decision_regions(X, y, classifier, resolution=0.02, test_idx = None):

    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v');
    colors = ("red", "blue", "lightgreen", "gray", "cyan");
    cmap = ListedColormap(colors[:len(np.unique(y))]);

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1;
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1;
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution));

    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape);
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap);
    plt.xlim(xx1.min(), xx1.max());
    plt.ylim(xx2.min(), xx2.max());

    # plot class examples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0],
                    y=X[y == cl, 1], alpha=0.8, c=colors[idx], label=cl, edgecolor="black");

    # highlight test examples
    if test_idx:
        # plot all examples
        X_test, y_test = X[test_idx, :], y[test_idx];

        plt.scatter(x=X_test[:, 0],
                    y=X_test[:, 1], facecolor="none", edgecolor="black", alpha=1.0,
                    linewidth=1, marker='o', s=100, label="test_set");