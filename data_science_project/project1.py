import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('data_science_project/data.csv')
# new_data=pd.read_csv('data_science_project/data.csv')
# print(df.head())
# print(new_data.head())
# print(new_data.info())
# print(new_data.isnull())
# print(df.info())
# print(df.isnull().sum())
# df=pd.read_csv('data_science_project/data.csv')
# new_month_bill_data=df['Monthly_Bill'].mean()
# new_data_usage_data=df['Total_Data_Usage'].mean()
# df['Monthly_Bill']=df['Monthly_Bill'].fillna(new_month_bill_data)
# df['Total_Data_Usage']=df['Total_Data_Usage'].fillna(new_data_usage_data)
# df['Churn']=df['Churn'].map({'Yes':1,'No':0})
# contract_mapping = {'Month-to-Month': 0, 'One Year': 1, 'Two Year': 2}
# df['Contract_Type'] = df['Contract_Type'].map(contract_mapping)
# print(df.isnull().sum())
# print(df.head())
# --- STEP 3: VISUALIZATION (THE DETECTIVE WORK) ---

# # 1. Set the size of the "Paper" (Canvas)
plt.figure(figsize=(6, 4))

# 2. Draw the Boxplot
# We compare: Churn (Left/Stayed) vs Monthly_Bill (Money)
sns.boxplot(x='Churn', y='Monthly_Bill', data=df)

# 3. Add a Title so we know what we are looking at
plt.title("Do Higher Bills Cause Churn? (0=No, 1=Yes)")

# 4. Show the Graph
plt.show()



