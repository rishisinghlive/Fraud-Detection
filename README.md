# Fraud-Detection
Fraud Detection Report

**Data Source: Kaggle   [https://www.kaggle.com/ealaxi/banksim1?select=bsNET140513_032310.csv**](https://www.kaggle.com/ealaxi/banksim1?select=bsNET140513_032310.csv)**

**This is a synthetic data which simulates the real life banking transection. This dataset have 594643 records out of them only 7200 is fraud. The dataset is having 9 independent feature and 1 dependent feature.**

**Target: Create an app that can detect the fraud Transection**

**Approach: Transform the categories in categorical code, create synthetic data to reduce the imbalance between fraud and non-fraud transection and apply the machine learning and deep learning models. Will take the model and create an app where you give your transection detail and it will tell whether transection is fraud or genuine. Will push this app to Heroku**
# Data Preprocessing
## Data Description:

`		`**Step**: Step Ranges from 0 to 179 where 0 stands for day 1 and 179 stands for 180th day

**Customer**: It refers to Customer Id the data set has 4112 unique customer

**Age**: Category of age group where

0: <= 18 Years,

1: = 19-25,

2: = 26-35,

3: = 36-45,

4: = 46-55,

5: = 56-65,

6: = Above 65

U: = Unknown

**Gender**: Gender of the customer

**ZipcodeOri**: Zip code of customer

**Merchant**: Refers to Merchant Id there are total 50 unique merchants.

**ZipMerchant**: Zip code of Merchant. The zip code of all customer and the zip code of all merchant is same

**Category**: Category of purchase, There total 15 categories.

**Amount**: Amount spent on Purchase

**Fraud**: The Transection was fraud or not. Target Feature
# Feature Selection:
- Features ZipcodeOri and ZipMerchant are same and both is having only 1 pin code therefor I will drop these columns.
- Feature step is the information of the number of day and feature customer is customer id these features doesn’t seem any relation with target feature so we will drop them.

Status: Effective
# Transformation:
- **Problem**: Transform the categorical features into numerical
- **Approach**: Will apply cat codes 
- **Status**: Effective
# Handling imbalance Data:
- **Problem** : The dataset is highly imbalanced
- **Approach1**: Create synthetic data using SMOTE
- **Approach2**: Increase the class weight of imbalance class. 
# Model Building:
- **Logistic Regression:** Accuracy Score 0.9219203499902119.
- **K nearest neighbors:** Accuracy Score 0.9859816663687664
- **ANN Using class weights:**  Accuracy Score 0.9947954203436837
- **Naïve Bayes: Accuracy Score:** 0.9141579211670879
- **Decision Tree: Accuracy Score:** 0.9887053256049503
- **Random Forest: Accuracy Score:** 0.9902288724901905
# Deployment
**Will use streamlit module to create a website and deploy over Heroku platform.**

**Challenges**: Fill the detail of the transaction and it should transform it to categorical code.

**Approach**: create a data frame for each columns which will take class name as input and return the categorical code. 

**Status:** Effective.
