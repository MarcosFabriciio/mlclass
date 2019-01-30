import pandas
import sklearn.neighbors as neighbors
abalones = pandas.read_excel("dataset_processado.xlsx");
test = pandas.read_excel("app_processado.xlsx");
knn = neighbors.KNeighborsClassifier
testData = abalones["type"]
trainingData = abalones.drop(columns=["type"]);

knn.fit(self, trainingData, testData)
