from sklearn.datasets import load_iris, load_breast_cancer, load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


def run_ann(name, data):
    # Load Data
    X = data.data
    y = data.target

    # Train-Test Split (stratified to preserve class distribution)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Feature Scaling (fit on train only, then apply to test)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Create ANN (one hidden layer of 10 neurons, sigmoid activation)
    model = MLPClassifier(
        hidden_layer_sizes=(10,),
        activation='logistic',
        max_iter=2000,
        random_state=42
    )

    # Train Model
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Evaluation
    accuracy = accuracy_score(y_test, y_pred)
    print(f"{name} Dataset Accuracy: {accuracy:.4f}")


if __name__ == "__main__":
    run_ann("Iris", load_iris())
    run_ann("Breast Cancer", load_breast_cancer())
    run_ann("Wine", load_wine())
