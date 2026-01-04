import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
df = pd.read_csv("student-mat.csv", sep=';')
df['pass'] = df['G3'].apply(lambda x: 1 if x >= 10 else 0)
X = df.loc[:, ['studytime', 'absences', 'G1', 'G2']]
y = df.loc[:, 'pass']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
sns.countplot(x='pass', data=df)
plt.title("Student Pass vs Fail")
plt.show()