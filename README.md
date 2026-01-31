# SCT_DS_03
Implementation of a Decision Tree Classifier to predict customer term deposit subscriptions using the UCI Bank Marketing dataset. This project includes data exploratory analysis via Excel Pivot Tables and a predictive model built with Python (Scikit-Learn).
Objective: Build a decision tree classifier to predict whether a customer will purchase a product or service (subscribe to a term deposit) based on their demographic and behavioral data.

1. Dataset Overview
Dataset Name: Bank Marketing Dataset.
Source: UCI Machine Learning Repository.
Total Instances: 45,211 instances related to direct marketing campaigns (phone calls) of a Portuguese banking institution.
Features: 16 attributes including age, job, marital status, education, and call duration.
Target Variable (y): Predicts if the client will subscribe to a term deposit ("yes" or "no").
2. Exploratory Data Analysis (Excel)
You performed a successful analysis using Excel Pivot Tables and Charts to identify key drivers for the model:
Job Category Insight: Your Pivot Table analysis shows that retired individuals (0.23 average) and students (0.22 average) have the highest subscription rates.
Visualization: You created a bar chart showing the "Average of y" across different job roles, highlighting that specialized demographics are more likely to subscribe.
3. Model Logic (Decision Tree Structure)
You designed a visual decision tree in Excel to represent the predictive logic:
Root Node: CALL DURATION > 200S? (Identifying call length as the primary filter).
Branch 1 (Yes): Splits into retired and Student demographics, leading to a PREDICTION: SUBSCRIBE (YES).
Branch 2 (No): Leads to a check for Previous campaign Success, resulting in a PREDICTION: NO SUBSCRIBE if the criteria aren't met.
4. Technical Implementation (Python)
You developed a Python script (TASK3.py) to automate the classification:
Libraries: Used pandas, matplotlib, and sklearn (LabelEncoder, DecisionTreeClassifier).
Preprocessing: Converted categorical text data into numerical format using Label Encoding.
Current Status: Your code successfully imports the necessary tools but requires the bank-full.csv file to be in the same directory to resolve the FileNotFoundError.
5. Repository Details (GitHub)
Repository Name: SCT_DS_03.
Description: "Implementation of a Decision Tree Classifier to predict customer term deposit subscriptions using the UCI Bank Marketing dataset. This project includes data exploratory analysis via Excel Pivot Tables and a predictive model built with Python (Scikit-Learn)".
