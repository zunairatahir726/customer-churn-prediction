# Customer Churn Prediction Using Machine Learning

## Project Overview

This project develops an end-to-end **Customer Churn Prediction System** using Machine Learning. The goal is to predict whether a telecommunications customer is likely to churn based on customer usage, service, demographic, and value-related features.

The project includes data preprocessing, exploratory data analysis, machine learning model development, model comparison, Random Forest optimization, explainability considerations, and deployment through an interactive Streamlit dashboard.

## Dataset

The project uses the **Iranian Churn Dataset** from the UCI Machine Learning Repository.

The dataset contains customer-related features such as:

* Call failures
* Complaints
* Subscription length
* Charge amount
* Seconds of use
* Frequency of use
* Frequency of SMS
* Number of distinct calls
* Age group
* Tariff plan
* Customer status
* Age
* Customer value

The target variable represents whether a customer has churned.

## Project Workflow

1. Data loading and inspection
2. Data preprocessing
3. Exploratory Data Analysis
4. Feature preparation
5. Machine Learning model development
6. Model comparison
7. Random Forest hyperparameter tuning
8. Model evaluation and error analysis
9. Explainability analysis
10. Streamlit dashboard deployment

## Machine Learning Models

The following models were explored:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

The Random Forest model was selected and optimized for the final prediction system.

## Evaluation

The models were evaluated using classification metrics such as:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

## Deployment

The final trained model was integrated into an interactive **Streamlit dashboard**.

The application allows users to enter customer information and receive an immediate churn prediction.

## Project Structure

```text
customer-churn-prediction/
│
├── paper/
│   ├── customer_churn_paper.tex
│   └── customer_churn_paper.pdf
│
├── notebooks/
├── app.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/customer-churn-prediction.git
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Streamlit

## Author

**Zunaira Tahir**

BSc Artificial Intelligence
AI & Machine Learning Internship
