# Employee Salary Prediction using Feedforward Neural Network

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error
import numpy as np

# ----------------------------------------------------
# Dataset
# [Age, Monthly charges, Tenure, Number of complaints,Customer support calls]
# ----------------------------------------------------
X = [
    [25,500,12,1,2],
    [30,700,24,0,1],
    [45,1200,6,5,8],
    [50,1500,5,6,10],
    [28,600,18,1,16],
    [35,800,30,0,0],
    [48,1400,4,7,9],
    [52,1600,3,8,12],
    [27,550,20,0,1],
    [42,1300,8,4,7]
]

# Salary Output
y = [0,0,1,1,0,
     0,1,1,0,1]
print(len(X), len(y))


# ----------------------------------------------------
# Split data
# ----------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)


# ----------------------------------------------------
# Create FNN Model
# ----------------------------------------------------
model = MLPRegressor(
    hidden_layer_sizes=(6,),
    activation='relu',
    solver='lbfgs',        # better for very small dataset
    max_iter=5000,
    random_state=42
)

# ----------------------------------------------------
# Train Model
# ----------------------------------------------------
model.fit(X_train, y_train)

# ----------------------------------------------------
# Predict on test data
# ----------------------------------------------------
pred= model.predict(X_test)



print("Actual output   :", y_test)
print("Predicted output  :", pred)

# Error
error = mean_absolute_error(y_test,pred)
print("\nAverage Error:", error)


new_cust = [[46,1450,5,6,9]]
#new_cust_scaled = X.transform(new_cust)

output = model.predict(new_cust)
#output = y.inverse_transform(output_scaled.reshape(-1, 1))

print("\nPredicted Output for New Customer:", output)