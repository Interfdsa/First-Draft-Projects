import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
# from sklearn.utils import shuffle
# import matplotlib.pyplot as pyplot
# import pickle
# from matplotlib import style
results = [] #list needed for average accuracy
iterations = 1000
i=0
for x in range(iterations):
#while i < 0.93:
    data = pd.read_csv("student-mat.csv", sep=";") # Since our data is seperated by semicolons we need to do sep=";"
    data=data[["G1", "G2", "G3", "studytime", "failures", "absences", "traveltime"]] #these are all the attributes ive decided to use to predict the outcome. commonly known as Features
    predict = "G3" #the predicted variable known as the label
    X = np.array(data.drop([predict],1)) #this array contains all the features (minus the predicted one)
    y = np.array(data[predict]) #this array contains all the labels (so just "G3"# )
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split( X, y, test_size=0.1)
    #the code above creates 4 variables 2 test and 2 training ones. The training data is 90% of our data size, the test uses the last 10% to validate the results.
    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    acc=linear.score(x_test, y_test)
    #print(acc) for debugging
    #i=acc
    #print(i)
    results.append(acc) #to get an average value this adds the accuraccy "acc" to a list
avg= sum(results)/len(results) #the list is summed and divided by the number of items in it
print("the average prediction accuracy after", iterations ,"iterations is", round(avg*100, 5), "%")
