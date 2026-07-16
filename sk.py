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
