import numpy as np
import csv
with open("data2.csv", 'r') as f: 
    reader = csv.reader(f)
    feature_set = np.array(list(list(rec) for rec in csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)))
with open("datar.csv", 'r') as f1: 
    reader = csv.reader(f1)
    labels = np.array(list(list(rec) for rec in csv.reader(f1, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)))
np.random.seed(42)  
weights = np.random.rand(7,1)  
bias = np.random.rand(1)  
lr = 0.2
def sigmoid(x):  
    return 1/(1+np.exp(-x))
def sigmoid_der(x):  
    return sigmoid(x)*(1-sigmoid(x))
epoch = 1
x = 1
print(weights,bias)
for epoch in range(2000):
#while (abs(x) > .001):
    inputs = feature_set

    # feedforward step1
    XW = np.dot(feature_set, weights) + bias

    #feedforward step2
    z = sigmoid(XW)


    # backpropagation step 1
    error = z - labels
    x = error.sum()
    #print(epoch,x)

    # backpropagation step 2
    dcost_dpred = error
    dpred_dz = sigmoid_der(z)

    z_delta = dcost_dpred * dpred_dz

    inputs = feature_set.T
    weights -= lr * np.dot(inputs, z_delta)

    for num in z_delta:
        bias -= lr * num
    #epoch = epoch + 1
print(weights,bias,x)
to_predict = np.array([1,0,1,0,1,1,1])  
result = sigmoid(np.dot(to_predict, weights) + bias)  
print('Probability of not getting layoff for the data set:1,0,1,0,1,1,1 is:',result)
