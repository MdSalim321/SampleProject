# 1. Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC
import pandas as pd

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# 1. Logistic Regression
model1 = LogisticRegression()
model1.fit(X_train, y_train)
pred1 = model1.predict(X_test)
print("1. Logistic Regression Accuracy:", accuracy_score(y_test, pred1))


# 2. Decision Tree Classifier
model2 = DecisionTreeClassifier()
model2.fit(X_train, y_train)
pred2 = model2.predict(X_test)
print("\n2. Decision Tree Accuracy:", accuracy_score(y_test, pred2))


# 3. Random Forest Classifier
model3 = RandomForestClassifier()
model3.fit(X_train, y_train)
pred3 = model3.predict(X_test)
print("\n3. Random Forest Accuracy:", accuracy_score(y_test, pred3))


# 4. K-Nearest Neighbors
model4 = KNeighborsClassifier()
model4.fit(X_train, y_train)
pred4 = model4.predict(X_test)
print("\n4. KNN Accuracy:", accuracy_score(y_test, pred4))


# 5. Support Vector Machine
model5 = SVC()
model5.fit(X_train, y_train)
pred5 = model5.predict(X_test)
print("\n5. SVM Accuracy:", accuracy_score(y_test, pred5))


# 6. Naive Bayes
model6 = GaussianNB()
model6.fit(X_train, y_train)
pred6 = model6.predict(X_test)
print("\n6. Naive Bayes Accuracy:", accuracy_score(y_test, pred6))


# 7. Confusion Matrix
print("\n7. Confusion Matrix (Logistic Regression):\n", confusion_matrix(y_test, pred1))


# 8. Classification Report
print("\n8. Classification Report (Decision Tree):\n", classification_report(y_test, pred2))


# 9. Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("\n9. First 5 rows of Scaled Features:\n", X_scaled[:5])


# 10. Label Encoding Example
data = pd.DataFrame({'Gender': ['Male', 'Female', 'Female', 'Male']})
le = LabelEncoder()
data['Gender_encoded'] = le.fit_transform(data['Gender'])
print("\n10. Label Encoding:\n", data)
