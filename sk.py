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
