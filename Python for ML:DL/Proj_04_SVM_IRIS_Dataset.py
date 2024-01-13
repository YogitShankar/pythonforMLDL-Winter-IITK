import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import datasets






plt.scatter(X[:, 0], X[:, 1], c = z)
plt.suptitle('SVM IRIS Data')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.grid(1,which='both')
plt.axis('tight')
plt.show()
