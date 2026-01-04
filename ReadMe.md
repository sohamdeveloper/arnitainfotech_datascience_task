# 🎓 Student Performance Prediction using Machine Learning

This project aims to predict student academic performance (Pass/Fail) using machine learning techniques based on academic and behavioral attributes.

---

## 📌 Problem Statement

To analyze student data and predict whether a student will pass or fail based on factors such as study time, absences, and previous grades.

---

## 📂 Dataset

- **Name:** Student Performance Dataset
- **Source:** UCI Machine Learning Repository
- **Records:** 395 students
- **Attributes Used:**
  - Study Time
  - Absences
  - First Period Grade (G1)
  - Second Period Grade (G2)
  - Final Grade (G3)

---

## 🧹 Data Cleaning & Labeling

- Removed missing and irrelevant values
- Selected important academic features
- Created a target label:
  - `1` → Pass (Final Grade ≥ 10)
  - `0` → Fail (Final Grade < 10)

---

## 📊 Exploratory Data Analysis (EDA)

EDA was performed to understand data distribution and relationships:

- Pass vs Fail distribution
- Effect of study time on results
- Impact of absences
- Correlation analysis using heatmap

---

## 🤖 Machine Learning Model

- **Algorithm Used:** Logistic Regression
- **Type:** Supervised Classification
- **Train-Test Split:** 80% Training, 20% Testing

---

## 📈 Results

- Achieved good prediction accuracy
- Previous grades (G1, G2) strongly influence final performance
- Absences negatively affect student results

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- VS Code
- GitHub

---

## 📁 Project Structure

student-performance-prediction/

│── student-mat.csv  
│── cleaned_student_performance.csv  
│── cleaning.py  
│── eda.py  
│── main.py  
│── README.md  
│── .gitignore

---

## 🚀 Future Enhancements

- Use advanced models like Random Forest or XGBoost
- Predict exact marks (Regression)
- Deploy model using Flask or Streamlit
- Add real-time student data

---

## 👤 Author

**Soham Tamboli**  
Data Science Intern
