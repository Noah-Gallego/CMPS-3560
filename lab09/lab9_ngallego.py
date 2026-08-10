import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()

X_data = iris.data

y_raw = iris.target # 0 = setosa, 1 = versicolor, 2 = virginica

y_data = np.where(y_raw == 2, 1, -1)

X_train, X_test, y_train, y_test = train_test_split(
    X_data, y_data, test_size=0.2, random_state=42, shuffle=True
)

def initialize(n):
    w = np.zeros(n)
    theta = 0.0
    return w, theta

def weighted_sum(w, x, theta):
    total = 0.0
    for i in range(len(w)):
        total += w[i] * x[i]
    total -= theta # wx - b
    return total

def activation(X):
    # Sign activation
    return 1 if X >= 0 else -1

def train(X_train, y_train, w, theta, lr=0.01, num_epochs=50):
    for epoch in range(num_epochs):
        updates_in_epoch = 0

        # Train Loop * epochs
        for x, y_d in zip(X_train, y_train):
            X = weighted_sum(w, x, theta)
            y = activation(X)

            if y != y_d:
                # Update weights
                for i in range(len(w)):
                    w[i] = w[i] + lr * x[i] * (y_d - y)

                # Update theta
                theta = theta - lr * (y_d - y)

                updates_in_epoch += 1

        # Convergence Check
        if updates_in_epoch == 0:
            break

    return w, theta

def test(X_test, y_test, w, theta):
    correct = 0
    for x, y_d in zip(X_test, y_test):
        X = weighted_sum(w, x, theta)
        y = activation(X)
        if y == y_d:
            correct += 1
    accuracy = correct / len(y_test)
    return accuracy

n_features = X_train.shape[1]
w, theta = initialize(n_features)
w, theta = train(X_train, y_train, w, theta)
accuracy = test(X_test, y_test, w, theta)
print(f"Test accuracy: {accuracy:.4f}")
