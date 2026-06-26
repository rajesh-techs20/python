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

OUTPUT
 Name  Marks Grade
0  Rajesh     98     A
1  Nandan     88     B
2   Adish     78     C
3  Venkat     99     A
4     Ram     67     C
     Name  Marks Grade
0  Rajesh     98     A
1  Nandan     88     B
     Name  Marks Grade
3  Venkat     99     A
4     Ram     67     C
0    98
1    88
2    78
3    99
4    67
Name: Marks, dtype: int64
count     5.000000
mean     86.000000
std      13.619838
min      67.000000
25%      78.000000
50%      88.000000
75%      98.000000
max      99.000000
Name: Marks, dtype: float64
     Name  Marks Grade
0  Rajesh     98     A
3  Venkat     99     A
0    Rajesh
1    Nandan
2     Adish
3    Venkat
4       Ram
Name: Name, dtype: str
86.0
99
67
