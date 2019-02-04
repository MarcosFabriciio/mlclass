import pandas as pd
import numpy as np
from os import listdir
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import requests

print('\n - Lendo o arquivo com o dataset sobre abalone')

# abalone = pd.read_csv('abalone_min_max.csv')

# # Criando X and y par ao algorítmo de aprendizagem de máquina.
# print(' - Criando X e y para o algoritmo de aprendizagem a partir do arquivo')
# X,Y = abalone[abalone.columns[:-1]],abalone[abalone.columns[-1]]
# Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, stratify = Y, random_state=66, test_size=0.10)

# # Ciando o modelo preditivo para a base trabalhada
# print(' - Criando modelo preditivo')
# svm = SVC(kernel='rbf',gamma=5, C=100)
# svm.fit(Xtrain,Ytrain)

# #realizando previsões com o arquivo de
# print(' - Aplicando modelo e enviando para o servidor')
# abalone_app = pd.read_csv('abalone_app_min_max.csv')
# y_pred = svm.predict(abalone_app)
y_pred = pd.read_csv("respostas.csv")
# Enviando previsões realizadas com o modelo para o servidor
URL = "https://aydanomachado.com/mlclass/03_Validation.php"

#TODO Substituir pela sua chave aqui
DEV_KEY = "Ponte de Safena"

# json para ser enviado para o servidor
data = {'dev_key':DEV_KEY,
        'predictions':y_pred.to_json(orient='values')}

# Enviando requisição e salvando o objeto resposta
r = requests.post(url = URL, data = data)

# Extraindo e imprimindo o texto da resposta
pastebin_url = r.text
print(" - Resposta do servidor:\n", r.text, "\n")

