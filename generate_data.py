import nnfs
from nnfs.datasets import spiral_data
import numpy as np

nnfs.init()
# Create dataset
X_train, y_train = spiral_data(samples=10000, classes=3)
X_test, y_test = spiral_data(samples=1000, classes=3)

# Shuffle train dataset
keys_train = np.array(range(X_train.shape[0]))
np.random.shuffle(keys_train)
X_train = X_train[keys_train]
y_train = y_train[keys_train]

np.savetxt("./data/X_train.csv", X_train, delimiter=",")
np.savetxt("./data/y_train.csv", y_train, delimiter=",")
np.savetxt("./data/X_test.csv", X_test, delimiter=",")
np.savetxt("./data/y_test.csv", y_test, delimiter=",")
