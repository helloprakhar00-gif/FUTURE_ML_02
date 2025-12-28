# Customer Churn Prediction System

## 📌 Project Overview
This project builds an end-to-end Machine Learning system to predict customer churn
for a telecom company. The goal is to identify customers at high risk of leaving
and provide actionable insights for retention strategies.

This project was completed as part of
**Machine Learning Task 2 – Churn Prediction System**
under the **Future Interns Internship Program**.

---

## 🎯 Business Problem
Customer churn leads to revenue loss and increased acquisition costs.
By predicting churn in advance, businesses can take proactive actions
to retain valuable customers.

---

## 📂 Dataset
- Telco Customer Churn Dataset (Kaggle)
- Each row represents a customer
- Target variable: `Churn` (Yes / No)

---

## 🛠️ Technologies Used
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- XGBoost
- Power BI (for dashboard)

---

## 🔍 Project Workflow
1. Data Understanding & Cleaning
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Model Building
   - Logistic Regression
   - Random Forest
   - XGBoost
5. Model Evaluation
6. Churn Probability Prediction
7. Feature Importance Analysis
8. Business Insights & Recommendations

---

## 📈 Model Performance
XGBoost was selected as the final model based on:
- Higher ROC-AUC
- Better recall for churned customers
- Strong overall performance

---

## 🔮 Key Insights
- Month-to-month contracts have the highest churn
- New customers are more likely to churn
- Higher monthly charges increase churn risk
- Auto-payment users are more loyal

---

## 💡 Business Recommendations
- Encourage long-term contracts
- Focus retention efforts on new customers
- Offer targeted discounts to high-risk customers
- Promote auto-payment options

---

## 📁 Output
- `churn_predictions.csv` contains churn probability and risk levels
- Ready for Power BI or business dashboards

---

## 🚀 How to Run
1. Clone the repository
2. Create and activate virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
