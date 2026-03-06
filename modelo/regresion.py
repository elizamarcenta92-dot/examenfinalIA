class RegresionLineal:

    def __init__(self,x,y):

        self.x=x
        self.y=y

        self.m=0
        self.b=0

    def calcular(self):

        n=len(self.x)

        sumx=sum(self.x)
        sumy=sum(self.y)

        sumxy=sum(self.x[i]*self.y[i] for i in range(n))
        sumx2=sum(self.x[i]**2 for i in range(n))

        self.m=(n*sumxy-sumx*sumy)/(n*sumx2-sumx**2)

        self.b=(sumy-self.m*sumx)/n

        return self.m,self.b

    def mse(self):

        n=len(self.x)

        error=0

        for i in range(n):

            pred=self.m*self.x[i]+self.b

            error+=(self.y[i]-pred)**2

        return error/n