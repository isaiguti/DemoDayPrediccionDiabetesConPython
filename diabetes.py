# -*- coding: utf-8 -*-
"""Diabetes-Proyecto-Machine-Learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nT-y8MVVJwpGRJVIaJKulxy9_obx8ydM

# Informacion del Dataset
* **Diabetes_012:** 0 = no diabetes | 1 = prediabetes | 2 = diabetes
* **HighBP:** 0 = sin PA alta | 1 = PA alta
* **HighChol:** 0 = sin colesterol alto | 1 = colesterol alto
* **CholCheck:** 0 = sin control de colesterol en 5 años | 1 = sí control de colesterol en 5 años
* **BMI:** Índice de masa corporal
* **Smoker:** ¿Ha fumado al menos 100 cigarrillos en toda su vida? [Nota: 5 paquetes = 100 cigarrillos] | 0 = no | 1 = sí
* **Stroke:** (Alguna vez dicho) que tuviste un derrame cerebral. | 0 = no | 1 = sí
* **HeartDiseaseorAttack:** enfermedad coronaria (CHD) o infarto de miocardio (IM) | 0 = no | 1 = sí
* **PhysActivity:** actividad física en los últimos 30 días - sin incluir el trabajo | 0 = no | 1 = sí
* **Fruits:** Consume fruta 1 o más veces al día | 0 = no | 1 = sí
* **Veggies:** Consume Verduras 1 o más veces al día | 0 = no | 1 = si
* **HvyAlcoholConsump:** Bebedores empedernidos (hombres adultos que beben más de 14 tragos por semana y mujeres adultas que beben más de 7 tragos por semana) | 0 = no | 1 = sí
* **AnyHealthcare** Tener algún tipo de cobertura de atención médica, incluidos seguros de salud, planes prepagos como HMO, etc. 0 = no | 1 = sí
* **NoDocbcCost:** ¿Hubo algún momento en los últimos 12 meses en que necesitó ver a un médico pero no pudo debido al costo? 0 = no | 1 = sí
* **GenHlth** Diría usted que en general su salud es: escala 1-5 1 = excelente | 2 = muy buena | 3 = buena | 4 = regular | 5 = mala
* **MentHlth:**Ahora, pensando en su salud mental, que incluye estrés, depresión y problemas con las emociones, ¿durante cuántos días durante los últimos 30 días su salud mental no fue buena? escala 1-30 días
* **PhysHlth:** Ahora, pensando en su salud física, que incluye enfermedades y lesiones físicas, ¿durante cuántos días durante los últimos 30 días su salud física no fue buena? escala 1-30 días
* **DiffWalk:** ¿Tiene serias dificultades para caminar o subir escaleras? 0 = no | 1 = sí
* **Sex:** 0 = femenino | 1 = masculino
* **Age:** Categoría de edad de 13 niveles (_AGEG5YR consulte el libro de códigos) 1 = 18-24 | 9 = 60-64 | 13 = 80 o más
* **Education:** Nivel de educación (EDUCA, consulte el libro de códigos) escala 1-6 1 = Nunca asistió a la escuela o solo al jardín de infantes | 2 = Grados 1 a 8 (primaria) | 3 = Grados 9 a 11 (algo de escuela secundaria) | 4 = Grado 12 o GED (Graduado de escuela secundaria) | 5 = Universidad 1 año a 3 años (Alguna universidad o escuela técnica) | 6 = Universidad 4 años o más (Graduado universitario)
* **Income:** Escala de ingresos (INGRESOS2 ver libro de códigos) escala 1-8 1 = menos de $10,000 | 5 = menos de $35,000 | 8 = $75,000 o más

# Edades
* 1	Age 18 - 24
* 2	Age 25 to 29
* 3	Age 30 to 34
* 4	Age 35 to 39
* 5	Age 40 to 44
* 6	Age 45 to 49
* 7	Age 50 to 54
* 8	Age 55 to 59
* 9	Age 60 to 64
* 10	Age 65 to 69
* 11	Age 70 to 74
* 12	Age 75 to 79
* 13	Age 80 or older
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/content/diabetes_012_health_indicators_BRFSS2015.csv")
df

def info_no_fc(_df):
  print(f'El dataset tiene {_df.shape[0]} filas y {_df.shape[1]} columnas.')

info_no_fc(df)

#info del conjunto de datos
df.info()

#Heatmap of correlation
plt.figure(figsize = (20,12))
sns.heatmap(df.corr(),annot=True)

df.isnull().sum()

df.hist(figsize = (20,20))

sns.countplot(df['Diabetes_012'])

# Checando filas duplicadas
duplicates = df[df.duplicated()]
print("Filas Duplicadas : ",len(duplicates))
duplicates

df_elim_dup = df
df_elim_dup.drop_duplicates(inplace = True)
info_no_fc(df_elim_dup)

no_dia= df[df['Diabetes_012'] == 0]
pre_dia = df[df['Diabetes_012'] == 1]
dia = df[df['Diabetes_012'] == 2]

pre_dia_os = pre_dia.sample(len(no_dia), replace=True)
dia_os = dia.sample(len(no_dia), replace=True)
pre_dia_os

df_new = pd.concat([pre_dia_os,dia_os, no_dia], axis=0)

df_new

df_new['Diabetes_012'].value_counts()

sns.countplot(df_new['Diabetes_012'])

X = df_new.drop("Diabetes_012", axis=1)
y = df_new.Diabetes_012

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

"""MinMaxScaler conserva la forma de la distribución original. No cambia significativamente la información incrustada en los datos originales. Tenga en cuenta que MinMaxScaler no reduce la importancia de los valores atípicos. El rango predeterminado para la función devuelta por MinMaxScaler es de 0 a 1."""

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

"""# Regresion Lineal

"""

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

X = df_new.drop("Diabetes_012", axis=1)
y = df_new.Diabetes_012

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

lr = LinearRegression()
lr.fit(X_train, y_train)

y_predict = lr.predict(X_test)

mean_squared_error(y_test, y_predict)

lr.score(X_test, y_test)

from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import cross_val_score
lr_1 = LinearRegression()
lr_1.fit(X_train, y_train)
print(f"R2 Train: {lr_1.score(X_train, y_train)}")
print(f"R2 Test: {lr_1.score(X_test, y_test)}")
print(f"Cross Val: {np.sum(cross_val_score(lr_1, X_train, y_train)) / 5}") # La validación cruzada sería preferible hacerla con TODOS nuestros datos

poly_2 = PolynomialFeatures(degree=2)
X_train_2 = poly_2.fit_transform(X_train)
X_test_2 = poly_2.fit_transform(X_test)

lr_2 = LinearRegression()
lr_2.fit(X_train_2, y_train)
print(f"R2 Train: {lr_2.score(X_train_2, y_train)}")
print(f"R2 Test: {lr_2.score(X_test_2, y_test)}")
print(f"Cross Val: {np.sum(cross_val_score(lr_2, X_train_2, y_train)) / 5}") # La validación cruzada sería preferible hacerla con TODOS nuestros datos

result = pd.DataFrame()

result["Regrsion Lineal"] = [0.23*100]

"""# Regresión logística"""

from sklearn.decomposition import PCA
 
pca = PCA(n_components = 20)
 
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)
 
explained_variance = pca.explained_variance_ratio_

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

#Performace Evaluation
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
 
print ("Confusion Matrix : \n", cm)

from sklearn.metrics import plot_confusion_matrix
plot_confusion_matrix(classifier,X_test,y_test,cmap='Blues')
plt.grid(False)

from sklearn.metrics import accuracy_score
print ("Accuracy : ", accuracy_score(y_test, y_pred))

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))

result["Regresión logística"] = [0.49]

"""# Naive Bayes"""

X = df_new.drop("Diabetes_012", axis=1)
y = df_new.Diabetes_012

from sklearn.decomposition import PCA
 
pca = PCA(n_components = 20)
 
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)
 
explained_variance = pca.explained_variance_ratio_

#Spliting the data in 80:20 training to testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train, y_train)

y_pred = gnb.predict(X_test)
 
# comparing actual response values (y_test) with predicted response values (y_pred)
from sklearn import metrics
print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)

#Performace Evaluation
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
 
print ("Confusion Matrix : \n", cm)

from sklearn.metrics import plot_confusion_matrix
plot_confusion_matrix(gnb,X_test,y_test,cmap='Blues')
plt.grid(False)

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))

result["Regresión logística"] = [48.32]

"""## 3. Random Forest

"""

# X = df_new.iloc[:, 1:].values
# y = df_new.iloc[:, 0].values
X = df_new.drop("Diabetes_012", axis=1)
y = df_new.Diabetes_012

from sklearn.decomposition import PCA
 
pca = PCA(n_components = 20)
 
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)
 
explained_variance = pca.explained_variance_ratio_

from sklearn.ensemble import RandomForestClassifier
 
model_1 = RandomForestClassifier(n_estimators = 300, criterion = 'entropy',
                             min_samples_split=10, random_state=0)

# fitting the model on the train data
model_1.fit(X_train, y_train)

# predicting values on test data
predictions = model_1.predict(X_test)

from sklearn import metrics
print("Random forest model accuracy(in %):", metrics.accuracy_score(y_test, predictions)*100)

#Performace Evaluation
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, predictions)
 
print ("Confusion Matrix : \n", cm)

from sklearn.metrics import plot_confusion_matrix
plot_confusion_matrix(model_1,X_test,y_test,cmap='Blues')
plt.grid(False)

from sklearn.metrics import classification_report
print(classification_report(y_test,predictions))

"""# Árboles de Decisión"""

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X = df_new.drop("Diabetes_012", axis=1)
y = df_new.Diabetes_012

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

tree_clf = DecisionTreeClassifier()
tree_clf.fit(X_train, y_train)

y_pred = tree_clf.predict(X_test)

matrix = confusion_matrix(y_test, y_pred)

from sklearn import metrics
print(f"Random forest Precisión del modelo  {metrics.accuracy_score(y_test, y_pred)*100}%")

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
 
print ("Confusion Matrix : \n", cm)

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))

from sklearn.metrics import plot_confusion_matrix
plot_confusion_matrix(tree_clf,X_test,y_test,cmap='Blues')
plt.grid(False)

result["Árboles de Decisión"] = [92.77]

"""# Funciones para calcular la precisión sensibilidad y especifidad"""

def calcular_precision(TP1, FN1, FN2, FP1, TP2, FN3, FP2, TP3, FP3):
    precision = (TP2 + TP3) / (FP1 + FP2 + TP2 + TP3)
    precision = precision * 100
    return precision

def calcular_sensibilidad(TP1, FN1, FN2, FP1, TP2, FN3, FP2, TP3, FP3):
    sensibilidad = TP1 / (TP1 + FN1 + FN2)
    sensibilidad = sensibilidad * 100
    return sensibilidad

def calcular_especificidad(TP, TN, FP, FN):
    especificidad = TN / (TN + FP)
    especificidad = especificidad * 100
    return especificidad

def calcular_accuracy(TP1, FN1, FN2, FP1, TP2, FN3, FP2, TP3, FP3):
    accuracy = TP1+TP2+TP3 / ( (TP1+TP2+TP3) + FP1+FP2+FP3 + FN1+FN2+FN3)
    accuracy = accuracy * 100
    return accuracy

"""#Random Forest"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

X = df_new.drop(columns=["Diabetes_012"])
y = df_new["Diabetes_012"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

rf_clf = RandomForestClassifier(n_estimators = 300, criterion = 'entropy',
                             min_samples_split=10, random_state=0)
rf_clf.fit(X_train, y_train)

y_pred = rf_clf.predict(X_test)

matrix = confusion_matrix(y_test, y_pred)
matrix

from sklearn.metrics import accuracy_score
print ("Accuracy : ", accuracy_score(y_test, y_pred))

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))

from sklearn.metrics import plot_confusion_matrix
plot_confusion_matrix(rf_clf,X_test,y_test,cmap='Blues')
plt.grid(False)

result["Random Forest"] = [94.98]

"""#Redes Neuronales"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 2.x
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

X = df_new.drop(columns=["Diabetes_012", "CholCheck", "Smoker", "Fruits", "Veggies", "HvyAlcoholConsump", "AnyHealthcare", "NoDocbcCost", "MentHlth", "Sex"])
y = df_new["Diabetes_012"]

# Normalmente aumento el número de neuronas hacia la parte intermedia de mi red y disminuyo hacia el final
# El número de neuronas de mis capas debe de ser un exponente de 2
# La última capa debe de tener la forma del output que requiero (por ejemplo, si mi output es 1 valor numérico, necesito 1 neurona)

b_l0 = tf.keras.layers.Dense(units=16, input_shape=([X.shape[1]]), activation="relu")
b_l1 = tf.keras.layers.Dense(units=32, activation="relu")
b_l2 = tf.keras.layers.Dense(units=8, activation="relu")
b_l3 = tf.keras.layers.Dense(units=4, activation="relu")
b_l4 = tf.keras.layers.Dense(units=1, activation="sigmoid")

b_model3 = tf.keras.Sequential([b_l0, b_l1, b_l2,b_l3, b_l4])

b_model3.compile(loss="mean_squared_error", optimizer=tf.keras.optimizers.Adam(0.001))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

history = b_model3.fit(X_train, y_train, epochs=50, verbose=True, validation_split=0.1)

fig = plt.figure(figsize=(10, 10))

plt.plot(history.history["loss"], label="loss")
plt.plot(history.history["val_loss"], label="val_loss")

plt.legend(loc="upper right");

y_predict = b_model3.predict(X_test)

r2_score(y_test, y_predict)

result["Redes Neuronales"] = [0.22*100]

"""# Arena de Clasificadores

"""

X = df_new.drop("Diabetes_012", axis=1)
y = df_new.Diabetes_012

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import CategoricalNB
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 15))
ax = fig.add_subplot()
X.hist(bins=100, ax=ax);

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

gaussian_nb = GaussianNB()
gaussian_nb.fit(X_train, y_train)
y_pred = gaussian_nb.predict(X_test)

gaussian_nb.fit(X_train, y_train)

y_pred = gaussian_nb.predict(X_test)

y.value_counts()

from sklearn import metrics
print(f"Random forest Precisión del modelo  {metrics.accuracy_score(y_test, y_pred)*100}%")

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
 
print ("Confusion Matrix : \n", cm)

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))

from sklearn.metrics import plot_confusion_matrix
plot_confusion_matrix(gaussian_nb,X_test,y_test,cmap='Blues')
plt.grid(False)

result["Arena de Clasificadores"] = [48.11]

"""# Resultados"""

result.columns

import plotly.graph_objects as go

fig = go.Figure(go.Bar(
            x=result.loc[0],
            y=result.columns,
            orientation='h'))

fig.show()