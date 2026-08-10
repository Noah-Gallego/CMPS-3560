from sklearn.datasets import load_iris, load_breast_cancer, load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def evaluate(name, loader, max_depth):
    data = loader()
    X = data.data
    y = data.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=max_depth,
        random_state=42,
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"{name} Accuracy:", round(accuracy, 4))


evaluate("Iris", load_iris, max_depth=3)
evaluate("Breast Cancer", load_breast_cancer, max_depth=5)
evaluate("Wine", load_wine, max_depth=4)
