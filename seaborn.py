import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#SEABORN BAR PLOT
data={
    "Names":["Rajesh","Ramesh","Chandan","Adish"],
    "Marks":[80,60,40,100]
}

df=pd.DataFrame(data)

sns.barplot(data=df,x="Names",y="Marks")
plt.title("Bar Chart")
plt.show()


#SEABORN LINEPLOT
dat={
    "Month":["January","Febraury","March","April"],
    "Sales":[100,200,120,80]
}

df=pd.DataFrame(dat)

sns.lineplot(x="Month",y="Sales",data=df,markers="o")


plt.title("Line Chart")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

#SEABORN SCATTER PLOT
da={
    "Hours":[1,2,3,4,5,6],
    "Marks":[30,40,50,60,70,80]
}

df=pd.DataFrame(da)

sns.scatterplot(x="Hours",y="Marks",data=df)

plt.title("Scatter Plot")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.show()

#SEABORN BOXEN PLOT
data = {
    "Marks":[90,36,78,56,99,81,65,35]
    }

df=pd.DataFrame(data)

sns.boxenplot(y="Marks",data=data)
plt.show()


#SEABORN HEATMAP PLOT
data=[
    [10,20,40],
    [30,60,50],
    [90,70,80]
]
df=pd.DataFrame(data)

sns.heatmap(df,annot=True,cmap="Blues")

plt.show()

#SEABORN countPLOT
data={
    "Grades":["A","B","C","A","A","B","C","A","A","C","B","A","A"]
}

df=pd.DataFrame(data)

sns.countplot(x="Grades",data=df)
plt.show()

data={
    "Marks":[80,56,97,55],
    "Age":[18,19,18,20],
    "Weight":[45,60,55,65]
}
df=pd.DataFrame(data)

sns.pairplot(df)

plt.show()
