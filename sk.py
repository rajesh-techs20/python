#LINEAR REGRESSION

import pandas as pd 
from sklearn.linear_model import LinearRegression
import joblib

data={
    "Area":[200,400,500,199,356],
    "price":[30000,60000,75000,29000,50000]
}
df=pd.DataFrame(data)

x=df[["Area"]]
y=df["price"]

model=LinearRegression()
model.fit(x,y)

prediction=model.predict(pd.DataFrame({"Area":[1700]}))
print("Prediction:",prediction)

#MOEL ACCURACY
score=model.score(x,y)
print(score)

joblib.dump(model,"hose.pkl")
print("Model saved successfully")

model=joblib.load("hose.pkl")
prediction=model.predict(pd.DataFrame({"Area":[1700]}))
print(prediction)

#DECISION TREE CLASSIFIER
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

data={
    "Marks":[40,25,90,70,50,20,34],
    "Result":["Pass","Fail","Pass","Pass","Pass","Fail","Fail"]
}

df=pd.DataFrame(data)

X=df[["Marks"]]
y=df["Result"]

model=DecisionTreeClassifier()
model.fit(X,y)

prediction=model.predict([[35]])
print(prediction)

#KNEIGHBORS 
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

data={
    "Marks":[1,2,3,4,5],
    "Result":["Fail","Fail","Pass","Pass","Pass"]
}

df=pd.DataFrame(data)

X=df[["Marks"]]
y=df["Result"]
model=KNeighborsClassifier()
model.fit(X,y)

prediction=model.predict(pd.DataFrame({"Marks":[2.6]}))
print(prediction)

RANDOM FOREST CLASSIFIER
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data={
    "Marks":[1,2,3,4,5],
    "Result":["fail","fail","pass","pass","pass"]
}
df=pd.DataFrame(data)
X=df[["Marks"]]
y=df["Result"]

model=RandomForestClassifier(n_estimators=10,random_state=42)
model.fit(X,y)

prediction=model.predict(pd.DataFrame({"Marks":[2.6]}))
print(prediction)

LOGISTIC REGRESSION
import pandas as pd
from sklearn.linear_model import LogisticRegression

data={
    "Marks":[1,2,3,4,5],
    "Result":[0,0,1,1,1]
}

df=pd.DataFrame(data)
X=df[["Marks"]]
y=df["Result"]
model=LogisticRegression()
model.fit(X,y)

prediction=model.predict(pd.DataFrame({"Marks":[2.4]}))
print(prediction)


SUPER VECTOR MACHINE
import pandas as pd
from sklearn.svm import SVC

data={
    "Marks":[1,2,3,4,5],
    "Result":["Fail","Fail","Pass","Pass","Pass"]
}

df=pd.DataFrame(data)
X=df[["Marks"]]
y=df["Result"]

model=SVC(kernel="linear")
model.fit(X,y)

prediction=model.predict(pd.DataFrame({"Marks":[2.4]}))
print(prediction)

NAIVE BAYES THEOREM
from sklearn.naive_bayes import GaussianNB

data={
    "Marks":[1,2,3,4,5],
    "Result":["Fail","Fail","Pass","Pass","Pass"]
}

df=pd.DataFrame(data)
X=df[["Marks"]]
y=df["Result"]

model=GaussianNB()
model.fit(X,y)

prediction=model.predict(pd.DataFrame({"Marks":[2.4]}))
print(prediction)

KCLUSTERS
import numpy as np
from sklearn.cluster import KMeans

X=np.array([
    [1],[2],[3],
    [10],[11],[12]
])

model=KMeans(n_clusters=2,random_state=42)
model.fit(X)

print(model.labels_)


MODEL ELEVATION
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score


actual=[1,0,1,0,1,1,0,1,1,0,0,0]
predic=[1,0,1,0,1,1,0,1,1,0,0,1]

accuracy=accuracy_score(actual,predic)#out of all predictions how many were actually correct
print(accuracy)
cm=confusion_matrix(actual,predic)#it gives  matrix TN FP FN TP
#TP those which actal and predict are both positive
# FP actaul are negative but predicted is positive
# TN both actual and predicted are negative
# FN actual is positive predicted is negativerint(cm)
print(cm)
ps=precision_score(actual,predic)#out of all true predictions how many were actually true
print(ps)
rs=recall_score(actual,predic) #out of all actual how many will model find it correctly
print(rs)
fp=f1_score(actual,predic)
print(fp)

from sklearn.preprocessing import StandardScaler 
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

data={
    "Age":[24,30,40],
    "Salary":[25000,80000,150000]
}
df=pd.DataFrame(data)
scaler=StandardScaler()
scaled=scaler.fit_transform(df)
print(scaled)
scaler=MinMaxScaler()
scaled=scaler.fit_transform(df)
print(scaled)
