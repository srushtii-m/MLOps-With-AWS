# import libraries
import torch
from torch.utils import data
import numpy
import matplotlib.pyplot as plt
from torch import nn 

# Create Dataset 
# Define a function to generate noisy data
def synthetic_data(m, c, num_examples):  
    """Generate y = mX + c + bias."""
    X = torch.normal(0, 1, (num_examples, len(m)))
    y = torch.matmul(X, m) + c
    y += torch.normal(0, 0.01, y.shape)
    return X, y.reshape((-1, 1))

true_m = torch.tensor([2, -3.4])
true_c = 4.2
features, labels = synthetic_data(true_m, true_c, 1000)

print('features:', features[0],'\nlabel:', labels[0])

# Visualize data set 
plt.figure()
plt.xlabel('features')
plt.ylabel('labels')
plt.scatter(features[:, (1)].detach().numpy(), labels.detach().numpy(), 1)
plt.show()  


# Read dataset and create small batch
def load_array(data_arrays, batch_size, is_train=True):  
    """Construct a PyTorch data iterator."""
    dataset = data.TensorDataset(*data_arrays)
    return data.DataLoader(dataset, batch_size, shuffle=is_train)

batch_size = 10
data_iter = load_array((features, labels), batch_size)

next(iter(data_iter))

# Define model & initialization
# Create single layer feed-forward network with 2 inputs and 1 outputs.
net = nn.Linear(2, 1)

#Initialize model params 
net.weight.data.normal_(0, 0.01)
net.bias.data.fill_(0)

# Define loss function
# mean squared error loss function
loss = nn.MSELoss()

#Define optimization algorithm 
# implements a stochastic gradient descent optimization method
trainer = torch.optim.SGD(net.parameters(), lr=0.03)


# Training 
num_epochs = 5
for epoch in range(num_epochs):
    for X, y in data_iter:
        l = loss(net(X) ,y)
        trainer.zero_grad() #sets gradients to zero
        l.backward() # back propagation
        trainer.step() # parameter update
    l = loss(net(features), labels)
    print(f'epoch {epoch + 1}, loss {l:f}')


# Results
m = net.weight.data
print('error in estimating m:', true_m - m.reshape(true_m.shape))
c = net.bias.data
print('error in estimating c:', true_c - c)
