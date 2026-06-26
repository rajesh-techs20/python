creating students.csv
Name,Marks,Grade
Rajesh,98,A
Nandan,88,B
Adish,78,C
Venkat,99,A
Ram,67,C


then creating pandas   text.py
import pandas as pd
df=pd.read_csv("students.csv")
print(df)
print(df.head(2)) #first 2 rows
print(df.tail(2)) #last 2 rows
print(df["Marks"])
print(df["Marks"].describe()) #summary of marks
print(df[df["Marks"]>90]) #filtering data
print(df["Name"]) #names
print(df["Marks"].mean()) #average marks
print(df["Marks"].max()) #maximum marks
print(df["Marks"].min()) #minimum marks
