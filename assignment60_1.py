# Import numpy for numerical operations
import math

import numpy as np

# ---------------------------------------------------------
# STEP 1 : Define Input Features
# ---------------------------------------------------------
# These are the inputs coming to the neuron (x1, x2, x3)

inputs = np.array([2,3])
# ---------------------------------------------------------
# STEP 2 : Define Weights
# ---------------------------------------------------------
# Each input has a corresponding weight (w1, w2, w3)
# Weights represent importance of each input

weights = np.array([0.4,0.6])

# ---------------------------------------------------------
# STEP 3 : Define Bias
# ---------------------------------------------------------
# Bias is an additional parameter that helps shift the output
# It allows the model to fit data better

bias = 0.5

# ---------------------------------------------------------
# STEP 4 : Calculate Weighted Sum (Z)
# ---------------------------------------------------------
# Formula:
# Z = (x1*w1 + x2*w2 + x3*w3) + bias
# Using numpy dot product for efficient calculation
#for .dot function it  array datatype should be there
z= np.dot(inputs, weights) + bias

# Manual calculation:
# (2.0 * 0.5) + (3.0 * 0.3) + (4.0 * 0.2) + 1.0
# = 1.0 + 0.9 + 0.8 + 1.0 = 3.7

# ---------------------------------------------------------
# STEP 1 : Sigmoid Activation Function
# ---------------------------------------------------------
# Sigmoid converts input into range (0, 1)
# Used for probability-based outputs

def sigmoid(z):
    """
    Sigmoid Function
    Formula: 1 / (1 + e^(-z))
    """
    return 1 / (1 + math.exp(-z))


  
    # -----------------------------------------------------
    # Apply Sigmoid Activation
    # -----------------------------------------------------

    y_hat = sigmoid(z)

    print("\nStep 2 : Activation Function")
    print("Activation Function : Sigmoid")
    print("Output (ŷ) =", y_hat)

    print("\n----- NEURON CALCULATION END -----\n")

    return z, y_hat

# ---------------------------------------------------------
# STEP 6 : Final Output
# ---------------------------------------------------------
# Pass the weighted sum through activation function

output = sigmoid(z)

# ---------------------------------------------------------
# STEP 7 : Display Results
# ---------------------------------------------------------

print("Inputs          :", inputs)
print("Weights         :", weights)
print("Bias            :", bias)
print("Weighted Sum (Z):", z)
print("Final Output    :", output)