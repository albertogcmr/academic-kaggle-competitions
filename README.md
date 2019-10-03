# Academic Kaggle Competitions: Repositorio para documentar competiciones en kaggle. 

## Intro

Este repositorio tiene como fin la documentación y fácil replicación de diferentes competiciones en [kaggle](https://www.kaggle.com/). 

## Entregables

Deberá hacerse una pull request a este repositorio con los siguientes requisitos mínimos: 
* Entrenar un mínimo de 4 modelos diferentes: 2 vistos en clase y 2 que no
* Realizar un mínimo de 4 técnicas de Feature Extraction and Engineering
* Documentación necesaria para poder reproducir el código
* El código en ficheros `.py` que permita reproducir el ejercicio

### Feature Extraction and Engineering

Posibles técnicas, además de estudiar el problema y sacar tus conclusiones: 

* One hot encoding
* Label encoding
* Get dummies
* PCA
* Consumo de API externa y/o web scraping

### Regresión

Posibles modelos de regresión: 

* LinearRegression
* DecisionTreeRegressor
* KNeighborsRegressor
* GradientBoostingRegressor
* RandomForestRegressor

### Clasificación

Posibles modelos de clasificación: 

* RandomForestClassifier
* GradientBoostingClassifier
* AdaBoostClassifier
* KNeighborsClassifier
* SVM

## Ejecución de script

En la carpeta source se encuentran los siguientes archivos:

* Input (dataset completo)
* Ouput (dataset procesado para hacer competición)
* main.py
* functions.py

El procedimiento es ejecutar el siguiente código, con el nombre del dataset que se encuentra en la carpeta Input y la columna target que se debe predecir.

```
python main.py -n "diamonds.csv -t "price"
```

Si el dataset es muy grande, se puede reducir el número de registros. El parámetro es opcional.

```
python main.py -n "cars.csv -t "price" -s 17000
```

En la carpeta Output aparecerán 4 archivos:

* Sample submission
* Train para los alumnos
* Test para los alumnos
* Test solution