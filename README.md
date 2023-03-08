# Response Model for Marketing Campaign

## Retail Marketing Analytics

Marketing analytics refers to the process of measuring and evaluating the effectiveness of marketing campaigns. It involves in the analysis of data related to customer behaviour, sales, market trends, and campaign performance **to help businesses make data driven decisions about their marketing strategies.**
 
The growth of supermarkets in most populated cities are increasing and market competitions are also high. In FMCG sector, data is important to make informed decisions that **can improve business operations, profitability, and retain customers.** Data is collected with every transaction(be it online or offline) about customers. This data is leveraged in the process of analyzing various aspects of a supermarket's operations, performance, and market position.
## Goal and Objectives
A supermarket chain is trying to run a marketing campaigns based on the past experiences of the other campaigns that have happened. The goal is to,
   
1) Build a **machine learning model** 

2) Understand **target audience**

3) Analyse customer behaviour such as **spend behavior and purchase habits** 

This would allow the supermarket to create well-targeted campaign. And can provide promotions and offers that appeal directly towards customers needs. Then, utilize the insights to achieve the following objectives, namely;
 
1) **Improve response rate**
    
2) **Maximize the ROI** towards the marketing campaign

3) Increase sales



## Project Details

### Data Collection: 

Source - We have used secondary data from Kaggle website.


### Data Exploration and Analysis: 
In this phase, the data is explored and analyzed to gain insights into the data characteristics, relationships, and patterns.

- Data Attribute Information given
- Build derived features: Customer age, tenure, total spend, total campaigns accepted for each cutomer
- **Event Rate** calculation
- Quality Analysis of data: Missing value, Duplicates and Null values. Missing value in found in 'Income' feature. No null and duplicate values
- Analyzed categorical, numerical features
- Outlier analysis: Using scatter plots, 5 number summary
- Statistics Summary
- Correlation check
- Visualization of correlation: Using heat map

### Data Preparation:	
- Missing Value Handling: Imputation with mean
- Zero variance check
- Feature selection
- Encode categorical features
- Define seperate dataframe for Target and Independent Features¶

### Model Selection and Training:
- Split data into test and train sets. Since the data is imbalanced, we use SMOTE and Random Undersampling to balance data.
- Scale data
- Model Buidling
	- Candidate models - Logistic regression, SVM, Decision tree, Random Forest, GBM, XGB classifier

	- Model Selection: Using cross_validate from sklearn. Scoring using **'Recall', 'Precision'**
    - Cross validation - Using Stratified KFold
	- Parameter tuning
	- **Performance Metrics: Recall, Precision, f1-score, ROC-AUC, Confusion matrix**
	
- **Model Selected: Logistic Regression(Using SMOTE sampling)**

- Extracted the important features by models coefficients

- Find predicted probabilities for Decile Analysis¶

### Probability Decile Analysis:
- Create Deciles based on the Model Probabilities: The whole dataset is divided into 10 equal groups

- Summarize the data at Decile Level

- Capture event rate, non event rate, count of the event, non event
	
- Create deciles from 1-10 with 1 having the high rank probabilities

- Find rank ordering

- Visualization: Gains chart, Lift chart



## 3 steps to boost marketing campaign

**Step 1: Find the target audience**

   From decile analysis, we can see that the customers with higher repsonse rate are in the first and second decile. So the first two decile, make the top 20% of customers that are, most likely to generate high percentage of overall revenue. Hence focusing on them should be a top priority.¶

- The response rate in the top 2 decile is 54 %
- 3.5% higher response rate, 80% reduction in marketing cost


**Step 2: Segmentation of target audience**
Customer Segementation is based on the campaign 'Response' for Recency(R), Frequency(F), and Monetary value(M) of the top 2 deciles. The best 20% of customers are then divided into different groups. The segment with highest response rate is given the first priority and the lowest response rate is given the last priority.

NOTE: We do not use RFM Analysis in the traditional way of setting scores and finding RFM score for each customer. Instead we use these 3 features for prioritization of target audience.

**Step 3: Recommendations**

   1) For the following products offers can be provided, namely, wine, meat, gold, fish.

   2) Send personalized notifications about discounts/offers to high spenders.

   3) Reward with offers for 'Refer a Friend'

   4) Send personalized email/message to encourage them to buy again.

   5) Loyalty Card program to gain points for multiple purchases that can be converted to discounts.
