from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC









svmcscore = accuracy_score(Ypred,Ytest)
print('Accuracy score of Linear SVM Classifier is',100*svmcscore,'%\n')

# Kernel SVM RBF - Gaussian Kernal
ksvmc = SVC(kernel = 'rbf')
ksvmc.fit(Xtrain, Ytrain)
Ypred = ksvmc.predict(Xtest)
svmcscore = accuracy_score(Ypred,Ytest)
print('Accuracy score of Kernel SVM Classifier with RBF is',100*svmcscore,'%\n')

