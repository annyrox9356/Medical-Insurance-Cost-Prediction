# Medical-Insurance-Cost-Prediction

## Project Overview
This project aims to predict the medical insurance costs of individuals based on their personal attributes such as age, gender, BMI, number of children, smoking habits, and region. Building an accurate prediction model can help both insurance companies and individuals understand the key factors driving medical expenses.

## Dataset
The dataset used for this project is the **Medical Cost Personal Datasets** sourced from Kaggle. 
- **Features:** `age`, `sex`, `bmi`, `children`, `smoker`, `region`
- **Target Variable:** `charges` (Medical Insurance Premium)

## Machine Learning Models Evaluated
To find the most accurate model, a comparative analysis of multiple regression algorithms was performed:
1. Linear Regression
2. Polynomial Regression (Degree = 4)
3. Support Vector Regression (SVR)
4. Decision Tree Regression
5. **Random Forest Regression (Best Model)**

## Results & Conclusion
After evaluating all models using R² Score and Root Mean Squared Error (RMSE), the **Random Forest Regressor** (with 150 estimators) significantly outperformed the rest.

- **Best Model R² Score:** ~0.87
- **Best Model RMSE:** ~4441.77

The results demonstrate that ensemble learning techniques like Random Forest capture the non-linear patterns in medical cost data much better than standard linear models, effectively solving the issue of overfitting seen in standalone Decision Trees.

## Repository Contents
- `Medical_Cost_Analysis.ipynb`: The complete notebook containing Data Preprocessing, Exploratory Data Analysis (EDA), Model Training, and Evaluation.
- `insurance.csv`: The dataset used for training the models.
- `rf_model.pkl`: The serialized (pickled) Random Forest model, ready for deployment.

## Future Scope
- Deploying the `.pkl` model using a web framework like Streamlit or Flask to create an interactive UI.
- Applying Hyperparameter Tuning (GridSearchCV/RandomizedSearchCV) to further optimize the Random Forest model.

---
*Created by [Anurag Tiwari] | Aspiring Machine Learning Engineer*
