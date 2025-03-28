# torch imports
import torch.nn.functional as F
import torch.nn as nn


class BinaryClassifier(nn.Module):
    """
    Define a neural network that performs binary classification.
    """

    ## Define the init function, the input params are required (for loading code in train.py to work)
    def __init__(self, input_features, hidden_dim, output_dim):
        """
        Initialize the model by setting up linear layers.
        Use the input parameters to help define the layers of your model.
        :param input_features: the number of input features in your training/test data
        :param hidden_dim: helps define the number of nodes in the hidden layer(s)
        :param output_dim: the number of outputs you want to produce
        """
        super(BinaryClassifier, self).__init__()

        # define any initial layers, here
        self.fc1 = nn.Linear(input_features, hidden_dim)
        self.drop = nn.Dropout(0.3)
        self.fc2 = nn.Linear(hidden_dim, output_dim)     
        self.sigma = nn.Sigmoid()

    
    ## Define the feedforward behavior of the network
    def forward(self, x):
        """
        Perform a forward pass of our model on input features, x.
        :param x: A batch of input features of size (batch_size, input_features)
        :return: A single, sigmoid-activated value as output
        """
        
        # define the feedforward behavior
        x = self.drop(F.relu(self.fc1(x)))
        x = self.fc2(x)
        x = self.sigma(x)
        return x
    
