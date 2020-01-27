# Neural_Network

This project is a part of the course AI taught in University of Tehran.
The goal is to implement a platform in which neural networks can be easily developed and used.
to do so, the basic elements of a neual network is implemented such as Input , 
Neuron , Performance and etc.
each object has a member function output wich is used in the forward pass and 
a member function dOutdX wich playes the gradient role in backward pass.
activation functio is sigmoid but the code has the flexibility for any other 
activation function.
the basic model described above suffers latency and excess computation so
a mechanism similar to cach was added to the final model.
