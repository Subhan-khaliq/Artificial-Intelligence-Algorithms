import random
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
def making_lists_for_clusters(k,l):
    if k==1:
        l.append(k)
        return l
    else:
        l.append(k)
        making_lists_for_clusters(k-1,l)
        return l
#It calculates the Distance between rows
def euclidean_distance(first_row, second_row):
    distance = 0
    for i in range(0,len(first_row)):         
        distance += pow((first_row[i] - second_row[i]),2)
    return math.sqrt(distance)
#It will caluates the average of mass in particular cluster
def average_mass(DataSet, cluster_list):
    #n is the cluster array
    average_mass = 0
    for i in range(0 , len(cluster_list)):
        average_mass += DataSet.loc[cluster_list[i], 'mass']
    
    average_mass = round(average_mass/len(cluster_list),2)
    return average_mass
#It will caluates the average of width in particular cluster
def average_width(DataSet, cluster_list):
    #n is the cluster array
    average_width = 0
    for i in range(0 , len(cluster_list)):
        average_width += DataSet.loc[cluster_list[i], 'width']
    average_width = round(average_width/len(cluster_list),2)
    return average_width

#It will caluates the average of height in particular cluster
def average_height(DataSet, cluster_list):
    #n is the cluster array
    average_height = 0
    for i in range(0 , len(cluster_list)):
        average_height += DataSet.loc[cluster_list[i], 'height']
    average_height = round(average_height/len(cluster_list),2)
    return average_height
#It will caluates the average of score in particular cluster
def average_score(DataSet, cluster_list):
    average_score = 0
    for i in range(0 , len(cluster_list)):
        average_score += DataSet.loc[cluster_list[i], 'color_score']
    average_score = round(average_score/len(cluster_list),2)
    return average_score
def Averages_of_Attributes(DataSet,t):
    print("New Centroid:")
    print("mass",average_mass(DataSet, t))
    print(" width: ",average_width(DataSet,t))
    print(" height: ",average_height(DataSet,t))
    print(" score: ",average_score(DataSet,t))
#General Algorithm which takes number of clusters and DataSet and return cluseters in the DataSet.
def k_mean(DataSet, k): 
    if k==0:
        print("Cluster must be greater than one")
        return
    random_numbers = []
    l=[]
    for i in range(0,k):
        random_numbers.append(random.randint(0, len(DataSet))) 
    # Computing Centroid
    distance = []
    for j in range(0, len(DataSet)):
        for i in range(0, k):
            dist = euclidean_distance(DataSet.loc[random_numbers[i]], DataSet.loc[j])
            distance.append((i+1, dist))
    distance.sort(key = lambda x:x[1])
    lists = [[] for _ in range(k)]
    l=making_lists_for_clusters(k,l)
    for i in range(0, len(DataSet)):
        for p in l:
            if (distance[i][0] == p):
                lists[p-1].append(i)
    for i in range(0,k):
        print("Cluster Number : ",i+1)
        print(lists[i])
        #Gives the Average of the Attributes
        Averages_of_Attributes(DataSet,lists[i])
#K can be anynumber greater than 1.
k_mean(fruits,2)
