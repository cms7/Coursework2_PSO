from random import random,seed
import numpy as np
import pandas as pd

from PSO import PSO
from functions import squared_error


print("Please choose an activation function of the following - sigmoid , tanh , relu ")
activation_func = input()

pso = PSO(100,12,20)
# function to intitialise a network taking adjustable numbers of inputs, hidden and outputs
# funtion will generate random weights for each input value, a bias is also genererated and will be the last element in the array
# e.g. 3 inputs: weights = [0.1 , 0.3 , 0.2, 0.6] where element [-1] is the bias
# number of hidden layers is configuarable through the funtion as w4 etc can be added easily 
def initialise_network(n_inputs, n_hidden, n_outputs):
    net = list()
    network = list()
    
    for i in range(100):
        net.append(pso.swarm[i].position)
    
    #for x in range(100):
    l11 = [{'weights': [net[0][i]for i in range(n_inputs)]}]
    l12 = [{'weights': [net[0][i+4]for i in range(n_inputs)]}]
    l21 = [{'weights': [net[0][i+8]for i in range(n_outputs)]}]
    l22 = [{'weights': [net[0][i+10]for i in range(n_outputs)]}]
    w = l11+l12+l21+l22
    network.append(w)
    
    print(network)
    return network

# activation functions which takes an input and produces a number between 0-1
def sigmoid(inpt):
    return 1/(1+np.exp(-inpt))

def tanh(inpt):
    return np.tanh(inpt)

def relu(inpt):
    return np.maximum(0,inpt)

# calculates the derivatives of the neuron output for all activation functions
def sigmoid_derivative(node_output):
    return sigmoid(node_output)*(1-sigmoid(node_output))

def tanh_derivative(node_output):
    return 1 - tanh(node_output)**2

def relu_derivative(node_output):
    if(node_output<0):
        return 0
    else: 
        return 1

# This will calculate the neurons activation value
def sum_weights(weights, inputs):
    # weights[-1] will act as the bias, this takes the last element in the array of weights, which previously was identified.
    sum = weights[-1]
    for i in range(len(weights)-1):
        sum += weights[i] * float(inputs[i])
    return sum

def forward_prop(net,row):
    inputs = row[:-1]
    for layer in net:
        temp = []
        for node in layer:
            #use the weighted sum of inputs and outputs and feed the result into an activation function defined by the used 
            #using conditional statements
            sum = sum_weights(node['weights'],inputs)
            if(activation_func == "sigmoid"):
                node['output'] = sigmoid(sum)
            elif(activation_func == "relu"):
                node['output'] = relu(sum)
            elif(activation_func == "tanh"):
                node['output'] = tanh(sum)
            else:
                #this is base case to make sure that there is a valid input for the activation function, else exit program
                print("Please enter a valid hyperparameter for activation function of the following: sigmoid , tanh, relu")
                exit()
            temp.append(node['output'])
        x,y = temp[2],temp[3]
    return x,y

# Network is trained over a fixed number of epochs which is set by the user
def train_net(net, data):
    #use previous functions developed for training
    forward_prop_output = forward_prop(net, data)
    coordinate = np.array(forward_prop_output)
    err = squared_error(coordinate)
    print(err)
        
        
   
#seed(1) ensures each test will use the same generated weights
seed(1)
dataset = pd.read_csv('DATASET.csv')
data = np.array(dataset,float)
row = data[0]

#sets the required inputs and outputs for dataset
n_inputs = len(dataset.columns) - 1
n_outputs = 2

#create and test network
net = initialise_network(n_inputs,2,n_outputs)
train_net(net,row)

