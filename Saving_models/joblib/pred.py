import pickle

#load the model
model = pickle.load('dibatic_81.pkl' , 'rb')
data = model.predict([[6,3,1,8,9,2,4,8]])

if data[0] == 0:
    print('person is not dibatic')
else:
    print('person is dibatic')