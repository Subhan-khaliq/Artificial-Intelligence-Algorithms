import pandas as pd
import numpy as np
import math
# Reading data from file
columns_name=['fruit_label','mass','width','height','color_score']
fruits = pd.read_csv("fruit_data_with_colors _1_.csv",usecols=columns_name)
#print (fruits)
# Taking mean
mass_m   = round(fruits['mass'][:50].mean(),2)
height_m = round(fruits['height'][:50].mean(),2)
# Fill the nan values with their respective column's mean
fruits['mass'] = np.where((fruits.mass.isnull() == True), mass_m,fruits['mass'])
fruits['height'] = np.where((fruits.height.isnull() == True), height_m,fruits['height'])
# set k's value
k=8
#Most_Frequent_Value in Neighbours
def most_frequent(List):
    return max(set(List), key = List.count)
#To calculate Euclidian_Distance
def Euclidian_Distance(length_of_traing_data,i):
    Distance=[]
    for x in range(length_of_traing_data):
        distance = pow((fruits['mass'][x]-fruits['mass'][i]),2)+pow((fruits['width'][x]-fruits['width'][i]),2)+pow((fruits['height'][x]-fruits['height'][i]),2)+pow((fruits['color_score'][x]-fruits['color_score'][i]),2)
        distance = math.sqrt(distance)
        Distance.append((distance,x))
    return Distance
#To get Neigbours
def get_neigbours(x):
    x.sort()
    neigbours=[]
    for i in range(k):
        neigbours.append(x[i][1])
    return neigbours
#To Predict Labels
def predicted_labels(x,i,D_set):
    labels=[]
    for t in x:
        labels.append(D_set['fruit_label'][t])
    most_freq=most_frequent(labels)
    D_set['fruit_label'][i] = most_freq
    return
#Main Algorithm of KNN
def KNN_Algorithm(D_set):
    Total_Length=len(D_set)
    i=50
    length_of_traing_data=50
    Distance=[]
    neig=[]
    while(i<Total_Length):
        Distance=Euclidian_Distance(length_of_traing_data,i)
        neig=get_neigbours(Distance)
        predicted_labels(neig,i,D_set)
        Distance=[]
        neig=[]
        i=i+1
    print(D_set)
KNN_Algorithm(fruits)