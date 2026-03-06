import math
from collections import Counter

class KNN:

    def __init__(self,x,y,clases,k=3):

        self.x=x
        self.y=y
        self.clases=clases
        self.k=k

    def distancia(self,x1,y1,x2,y2):

        return math.sqrt((x1-x2)**2+(y1-y2)**2)

    def predecir(self,xn,yn):

        distancias=[]

        for i in range(len(self.x)):

            d=self.distancia(xn,yn,self.x[i],self.y[i])

            distancias.append((d,self.clases[i]))

        distancias.sort(key=lambda x:x[0])

        vecinos=distancias[:self.k]

        clases=[v[1] for v in vecinos]

        resultado=Counter(clases).most_common(1)[0][0]

        return resultado