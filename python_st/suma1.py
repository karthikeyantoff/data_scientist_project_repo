# import pandas as pd
# data={
#     "cal":[234,543,321],
#     "durations":[6,5,4]
# }
# result=pd.DataFrame(data,index=["day1","day2","day3"])
# print(result.loc["day1"])
import pandas as pd
data=pd.read_csv('data.csv')
# x=data["Date"].mean()
# res=data.fillna({"Date":x})
print(data.head())