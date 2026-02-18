# MNIST Digit Classification Project

## Project Description
This project implements a machine learning pipeline to classify handwritten digits from the MNIST dataset using Logistic Regression with scikit-learn. The code is organized into modular functions for data loading, preprocessing, training, and evaluation.

## Installation
To set up the project environment, clone the repository and install the required dependencies using pip:

```bash
# Clone the repository
git clone <repository-url>
cd <repository-directory>

# Install dependencies
pip install -r requirements.txt
```

## Usage
The project is structured as a modular Python script. You can run the entire pipeline by executing the main script from the command line:

```bash
python mnist_classifier.py
```

Alternatively, you can import the functions into your own workflow:

```python
from mnist_classifier import load_mnist_data, preprocess_data, train_logistic_regression, evaluate_model

X, y = load_mnist_data()
X_train, X_test, y_train, y_test = preprocess_data(X, y)
model = train_logistic_regression(X_train, y_train)
evaluate_model(model, X_test, y_test)
```

## Model Performance
The model achieves an accuracy of approximately **91.0%** on the test set.

**Key Preprocessing Steps:**
- **Data Splitting**: 60% training and 40% testing split.
- **Feature Scaling**: Standard Scaling was applied to the pixel data to improve the convergence of the Logistic Regression model.
