## IMPORT LIBRARIES
import pandas as pd
import numpy as np

## LOAD DATASET
df= pd.read_csv("Dataset/payment_fraud.csv")
print(df.head())

## DATA UNDERSTANDING
print(df.shape)
print(df.info())
print(df.isnull().sum())

## DATA CLEANING
df.drop_duplicates(inplace=True)
print(df.shape)

## ANALYSIS 1
## how many transcations are fraud
## FRAUD VS GENUINE TRANSCATIONS
fraud_summary=(df["isFraud"].value_counts())
fraud_summary.to_csv("/Users/qyser/Desktop/financial_fraud_ananalysis/Outputs/fraud_summary.csv")

## ANALYSIS 2
## FRAUD BY TRANSACTION TYPES
fraud_type= (df[df["isFraud"]==1].groupby("type").size())
fraud_type.to_csv("/Users/qyser/Desktop/financial_fraud_ananalysis/Outputs/fraud_type.csv")

## ANALYSIS 3
## HIGH VALUE FRAUD TRANACTIONS
threshold= np.percentile(df["amount"],95)

## extract
high_value=df[df["amount"]>threshold]
high_value.to_csv("/Users/qyser/Desktop/financial_fraud_ananalysis/Outputs/high_value.csv",index=False)

## ANALYSIS 4
## TOP 10 LARGEST FRAUD TRANSACTION 
top_frauds=(df[df["isFraud"]==1].sort_values(by="amount",ascending=False).head(10))
top_frauds.to_csv("Outputs/top_frauds.csv")

## ANALYSIS 5
## ACCOUNNT BALANCE CHANGE ANALYSIS
df["BalanceChange"] = (
    df["oldbalanceOrg"]
    -
    df["newbalanceOrig"])
df[["amount","BalanceChange"]].to_csv("outputs/balance_change.csv",index=False)

## ANALYSIS 6
##TRANSACATION TYPE DISTIRBUTION

transaction_distribution = (
    df["type"]
    .value_counts()
)
transaction_distribution.to_csv(
    "outputs/transaction_distribution.csv"
)


## analysis 7
## fraud rate by tarnscation type

fraud_rate = (
    df.groupby("type")
    ["isFraud"]
    .mean()
    * 100
)
fraud_rate.to_csv(
    "outputs/fraud_rate.csv"
)

## ANALYSIS 8
## FARUD RISK SCORE
df["RiskScore"] = (
    df["amount"] /
    df["amount"].max()
) * 100

df[
    ["amount","RiskScore"]
].to_csv(
    "outputs/risk_score.csv",index=False)

print("successfully executed")




