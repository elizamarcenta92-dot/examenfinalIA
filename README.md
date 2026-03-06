# Proyecto Final – Implementación de Modelos de Inteligencia Artificial con Interfaz Gráfica

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de una aplicación que implementa algoritmos de aprendizaje supervisado desde sus fundamentos matemáticos, integrando una interfaz gráfica de usuario (GUI) que permite interactuar con los datos, visualizar resultados y realizar predicciones.

El objetivo principal es comprender y aplicar los principios matemáticos detrás de los algoritmos de **Regresión Lineal Simple** y **K-Nearest Neighbors (K-NN)**, evitando el uso de librerías que automaticen el aprendizaje automático.

La aplicación permite cargar conjuntos de datos, visualizar gráficamente la información y generar predicciones utilizando los algoritmos implementados manualmente.

---

## Objetivo

Desarrollar una aplicación funcional que:

- Implemente algoritmos de aprendizaje supervisado desde sus bases matemáticas.
- Permita la interacción con los datos mediante una interfaz gráfica.
- Visualice los resultados mediante gráficos dinámicos.
- Permita realizar predicciones basadas en los modelos entrenados.

---

## Restricciones Técnicas

### Lógica del Algoritmo

Está prohibido utilizar librerías que implementen directamente algoritmos de Machine Learning como:

- Scikit-learn  
- PyCaret  
- TensorFlow  
- Keras  

Toda la lógica matemática de los algoritmos fue implementada manualmente.

### Lenguaje y Librerías

El proyecto fue desarrollado utilizando:

- Python

Librerías utilizadas únicamente para soporte visual y manejo de datos:

- Pandas (manejo de archivos CSV)  
- NumPy (operaciones matemáticas)  
- Matplotlib (visualización de gráficos)  
- Flask (interfaz web)

---

## Algoritmos Implementados

### 1. Regresión Lineal Simple

La regresión lineal se implementó utilizando el **método de mínimos cuadrados** para calcular la relación entre dos variables.

#### Fórmulas utilizadas

Pendiente:

m = ( n Σ(xy) − Σx Σy ) / ( n Σ(x²) − (Σx)² )

Intercepto:

b = ȳ − m x̄

Predicción:

y = mx + b

#### Métrica de Evaluación

Error Cuadrático Medio (MSE):

MSE = (1/n) Σ (yi − ŷi)²

#### Funcionalidades

- Carga de datos desde archivo CSV
- Cálculo automático de pendiente e intercepto
- Predicción de valores Y a partir de un valor X
- Visualización gráfica con línea de regresión

---

### 2. K-Nearest Neighbors (K-NN)

El algoritmo **K-NN** permite clasificar un punto nuevo basándose en la cercanía con otros puntos del dataset.

#### Distancia utilizada

Distancia Euclidiana:

d = √((x1 − x2)² + (y1 − y2)²)

#### Funcionamiento

1. Se calcula la distancia entre el punto nuevo y todos los puntos del dataset.
2. Se seleccionan los **K vecinos más cercanos**.
3. Se realiza una **votación por mayoría** entre las clases.
4. Se asigna la categoría resultante.

#### Funcionalidades

- Selección del valor de **K**
- Clasificación de nuevos puntos
- Visualización de puntos clasificados
- Representación gráfica de las clases

---

## Funcionalidades de la Aplicación

### 1. Módulo de Carga de Datos

Permite:

- Subir archivos CSV
- Ingresar datos manualmente
- Visualizar los datos cargados

---

### 2. Panel de Resultados

Muestra:

**Para Regresión**
- Ecuación de la recta generada
- Pendiente
- Intercepto
- Error Cuadrático Medio (MSE)

**Para KNN**
- Clase asignada al nuevo punto
- Vecinos más cercanos

---

### 3. Área de Visualización de Gráficos

La aplicación genera gráficos dinámicos.

**Regresión Lineal**
- Scatter plot de los datos
- Línea de tendencia

**KNN**
- Mapa de puntos
- Colores por clase