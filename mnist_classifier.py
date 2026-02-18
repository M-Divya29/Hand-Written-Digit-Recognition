from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

def load_mnist_data():
    """Load the MNIST dataset using fetch_openml."""
    mnist = fetch_openml('mnist_784', version=1, as_frame=False)
    return mnist.data, mnist.target

def preprocess_data(X, y, test_size=0.4, random_state=42):
    """Split data and apply standard scaling."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, y_train, y_test

def train_logistic_regression(X_train, y_train, max_iter=1000):
    """Instantiate and train a Logistic Regression model."""
    clf = LogisticRegression(max_iter=max_iter, solver='lbfgs', n_jobs=-1)
    clf.fit(X_train, y_train)
    return clf

def evaluate_model(model, X_test, y_test):
    """Predict and print the accuracy score."""
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {acc:.4f}")
    return acc

def main():
    """Main execution block for the end-to-end pipeline."""
    print("Loading data...")
    X, y = load_mnist_data()

    print("Preprocessing data...")
    X_train, X_test, y_train, y_test = preprocess_data(X, y)

    print("Training model (this may take a moment)...)")
    model = train_logistic_regression(X_train, y_train)

    print("Evaluating model...")
    evaluate_model(model, X_test, y_test)

if __name__ == '__main__':
    main()
