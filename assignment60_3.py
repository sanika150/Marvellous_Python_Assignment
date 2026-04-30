# Marvellous Binary Cross Entropy Demonstration
import math
# Marvellous MSE Loss Demonstration

def Marvellous_MSE(y_true, y_pred):
    n = len(y_true)
    total_error = 0

    for i in range(n):
        error = y_true[i] - y_pred[i]
        total_error += error ** 2   # Squared error

    mse = total_error / n
    return mse


# Sample Data
y_true = [10, 20, 30]
y_pred = [12, 18, 33]

loss = Marvellous_MSE(y_true, y_pred)

print("MSE Loss:", loss)

def Marvellous_Binary_CrossEntropy(y_true, y_pred):
    total_loss = 0
    n = len(y_true)

    for i in range(n):
        y = y_true[i]
        p = y_pred[i]

        # Avoid log(0)
        p = max(min(p, 0.999), 0.001)#to keep ans in range

        loss = -(y * math.log(p) + (1 - y) * math.log(1 - p))
        total_loss += loss

    return total_loss / n




loss = Marvellous_Binary_CrossEntropy(y_true, y_pred)
print("Binary Cross Entropy Loss:", loss)

