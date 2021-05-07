from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix, classification_report, accuracy_score

iris = load_iris()
iris_data = iris.data
iris_label = iris.target
print(iris_data)
print(iris_label)
print(iris_label.shape)

reshaped_iris_label = iris_label.reshape(1, 150)
print(reshaped_iris_label)
print(reshaped_iris_label.shape)

X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_label, test_size=0.33,
                                                    random_state=1)

classifier = SVC(C=5.0)
classifier.fit(X=X_train, y=y_train)

y_prediction = classifier.predict(X=X_test)
print("Prediction: ", y_prediction)
print("Ground truth: ", y_test)

print("Accuracy: ", accuracy_score(y_true=y_test, y_pred=y_prediction))

print("Classification report: ", '\n', classification_report(y_true=y_test, y_pred=y_prediction))

scores = cross_val_score(estimator=classifier, X=X_train, y=y_train, cv=10, scoring='accuracy')

print("Scores: ", scores)
print("Mean Scores: ", scores.mean())

y_prediction2 = classifier.predict(X=X_train)

print("Report", '\n', classification_report(y_true=y_train, y_pred=y_prediction2))
