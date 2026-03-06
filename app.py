from flask import Flask, render_template, request, jsonify
import pandas as pd
import math

app = Flask(__name__)

# ===============================
# REGRESION LINEAL
# ===============================

def regresion(x,y):

    n=len(x)

    sumx=sum(x)
    sumy=sum(y)

    sumxy=sum(x[i]*y[i] for i in range(n))
    sumx2=sum(x[i]**2 for i in range(n))

    m=(n*sumxy-sumx*sumy)/(n*sumx2-sumx**2)

    b=(sumy-m*sumx)/n

    errores=[(y[i]-(m*x[i]+b))**2 for i in range(n)]
    mse=sum(errores)/n

    return m,b,mse


# ===============================
# KNN
# ===============================

def distancia(a,b):

    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


def knn(datos,punto,k):

    distancias=[]

    for d in datos:

        d1=distancia((d[0],d[1]),punto)

        distancias.append((d1,d[2]))

    distancias.sort()

    vecinos=distancias[:k]

    votos={}

    for v in vecinos:

        votos[v[1]]=votos.get(v[1],0)+1

    return max(votos,key=votos.get)


# ===============================
# RUTAS
# ===============================

@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/regresion")
def pagina_regresion():
    return render_template("regresion.html")


@app.route("/knn")
def pagina_knn():
    return render_template("knn.html")


# ===============================
# API REGRESION
# ===============================

@app.route("/api/regresion",methods=["POST"])
def api_regresion():

    archivo=request.files["archivo"]

    df=pd.read_csv(archivo)

    x=df.iloc[:,0].tolist()
    y=df.iloc[:,1].tolist()

    m,b,mse=regresion(x,y)

    return jsonify({
        "x":x,
        "y":y,
        "m":m,
        "b":b,
        "mse":mse
    })


# ===============================
# API KNN
# ===============================

@app.route("/api/knn",methods=["POST"])
def api_knn():

    archivo=request.files["archivo"]

    x=float(request.form["x"])
    y=float(request.form["y"])
    k=int(request.form["k"])

    df=pd.read_csv(archivo)

    datos=[]

    for i in range(len(df)):

        datos.append([
            float(df.iloc[i,0]),
            float(df.iloc[i,1]),
            str(df.iloc[i,2])
        ])

    pred=knn(datos,(x,y),k)

    return jsonify({
        "datos":datos,
        "prediccion":pred,
        "nuevo":[x,y]
    })


if __name__=="__main__":
    app.run(debug=True)