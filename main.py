import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix

df = pd.read_csv("students.csv", sep=';')

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

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.countplot(x='pass', data=df, ax=axes[0])
axes[0].set_title("Student Pass vs Fail")

cm = confusion_matrix(y_test,y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[1])
axes[1].set_title("Confusion Matrix")
axes[1].set_xlabel("Predicted")
axes[1].set_ylabel("Actual")

plt.tight_layout()
plt.show()