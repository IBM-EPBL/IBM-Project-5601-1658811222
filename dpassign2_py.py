# -*- coding: utf-8 -*-
"""Copy of Datapreprocessing.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WxVr4_zlGeOOJbb-QfcwyPJobG6h-Aoe
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

df=pd.read_csv('Churn_Modelling.csv')
df.head()

df.shape

df.info()

df.isnull().any()

df.describe

df.Geography.unique()

df.Gender.value_counts()

df.Geography.value_counts()

df.NumOfProducts.value_counts()

df.HasCrCard.value_counts()

df.IsActiveMember.value_counts()

df.Exited.value_counts()

df.corr()

sns.displot(df.CreditScore)

sns.displot(df.Age)

sns.displot(df.Tenure)

sns.displot(df.Balance)

sns.displot(df.EstimatedSalary)

sns.lineplot(df.Age,df.Tenure)

sns.lineplot(df.HasCrCard,df.IsActiveMember)

sns.scatterplot(df.CreditScore,df.EstimatedSalary)

plt.pie(df.HasCrCard.value_counts(),[0,0],labels=['YES','NO'],autopct="%1.2f%%",colors=['Green','pink'])
plt.title('Credit Card')

plt.pie(df.NumOfProducts.value_counts(),[0.1,0.1,0.7,0.7],labels=['1','2','3','4'],autopct="%1.0f%%",colors=['pink','yellow','green','red'])
plt.title('Number of Products')

plt.pie(df.IsActiveMember.value_counts(),[0,0],labels=['YES','NO'],autopct="%1.2f%%",colors=['Green','pink'])
plt.title('Active Members')

plt.pie(df.Exited.value_counts(),[0,0],labels=['YES','NO'],autopct="%1.2f%%",colors=['YELLOW','pink'])
plt.title('Credit Card')

sns.barplot(df.Age.value_counts().index,df.Age.value_counts())

sns.barplot(df.Tenure.value_counts().index,df.Tenure.value_counts())

df.hist(figsize=(10,15))

"""Outlier Detection

"""

sns.boxplot(df.Balance)

"""Outlier removal using IQR"""

q1=df.Balance.quantile(0.25)  
q3=df.Balance.quantile(0.75)

IQR=q3-q1

upper_limit= q3 + 1.5*IQR
lower_limit= q1 - 1.5*IQR

df=df[df.Balance<upper_limit]

sns.boxplot(df.Balance)

"""Outlier removal with percentile

"""

sns.boxplot(df.Balance)

p99= df.Balance.quantile(0.99)
p99

df.describe()

df=df[df.Balance<=p99]

sns.boxplot(df.Balance)

df.shape

df.head()

"""Encoding

Label encoding
"""

from sklearn.preprocessing import LabelEncoder

le=LabelEncoder()

df.Gender=le.fit_transform(df.Gender)
df.Geography=le.fit_transform(df.Geography)

df.head()

"""One Hot Encoding"""

df_new=pd.get_dummies(df,columns=['Surname'])
df_new.head()

df_new.corr()

df_new.corr().Balance.sort_values(ascending=False)

plt.figure(figsize=(10,8))

df_new.head()

"""X and Y Split"""

y=df_new['Balance']
y

X=df_new.drop(columns=['Balance'],axis=1)
X.head()

"""Scaling"""

from sklearn.preprocessing import scale

X_scaled=pd.DataFrame(scale(X),columns=X.columns)
X_scaled.head()

"""Train test split"""

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X_scaled,y,test_size=0.3,random_state=0)

from google.colab import drive
drive.mount('/content/drive')