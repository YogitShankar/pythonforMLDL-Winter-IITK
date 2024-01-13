from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA








# LDA for dimensionality reduction
Xl = lda.transform(X)
plt.figure(1);
plt.scatter(Xl[:, 0], Xl[:, 1], c = Y)
plt.suptitle('LDA IRIS Data')
plt.xlabel('LDA 1')
plt.ylabel('LDA 2')
plt.grid(1,which='both')
plt.axis('tight')
plt.show()

# PCA for dimensionality reduction
pca = PCA(n_components=2);
Xp = pca.fit(X).transform(X)
plt.figure(2);
plt.scatter(Xp[:, 0], Xp[:, 1], c = Y)
plt.suptitle('PCA IRIS Data')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.grid(1,which='both')
plt.axis('tight')
plt.show()


