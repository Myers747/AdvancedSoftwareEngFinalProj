import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

# Define a simple feedforward neural network
class SimpleNN(nn.Module):
    """
    A basic feedforward neural network with one hidden layer.
    - input_size: Number of input features
    - hidden_size: Number of neurons in the hidden layer
    - output_size: Number of output features
    """
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)  # First fully connected layer
        self.relu = nn.ReLU()                         # Activation function
        self.fc2 = nn.Linear(hidden_size, output_size) # Second fully connected layer

    def forward(self, x):
        """
        Forward pass through the network.
        - x: Input tensor
        Returns: Output tensor
        """
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Define a training loop for the neural network
def train_model():
    """
    Trains the SimpleNN model using randomly generated data.
    - Trains for 10 epochs
    - Prints the loss after each epoch
    """
    # Initialize the model, loss function, and optimizer
    model = SimpleNN(input_size=10, hidden_size=20, output_size=1)
    criterion = nn.MSELoss()  # Mean Squared Error Loss
    optimizer = optim.SGD(model.parameters(), lr=0.01)  # Stochastic Gradient Descent

    # Training loop
    for epoch in range(10):  # 10 epochs
        # Generate random inputs and targets
        inputs = torch.randn(32, 10)  # Batch of 32 with 10 features each
        targets = torch.randn(32, 1)  # Batch of 32 with 1 target value each

        # Reset gradients
        optimizer.zero_grad()
        
        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs, targets)  # Compute loss
        
        # Backward pass and optimization step
        loss.backward()
        optimizer.step()

        # Print loss for the current epoch
        print(f"Epoch [{epoch + 1}/10], Loss: {loss.item()}")

if __name__ == "__main__":
    # Train the model when the script is run
    train_model()
