import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
import time

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass', 'pedi', 'age' , 'class']


df = pd.read_csv(url, names = names)
print(df.head())

array = df.values

X, y = array[:,0:8] , array[:,8]

X_train, X_test, y_train , y_test = model_selection.train_test_split(X,y, test_size = 0.2, random_state = 101)

# training the model
model = LogisticRegression()
model.fit(X_train,y_train)

print("[INFO]- model has trained")

# accuracy
result = model.score(X_test, y_test)
print("[INFO]- model accuracy is {}".format(result))

# model saving
filename = 'dibatic_81.pkl' # .sav
joblib.dump(model ,filename)