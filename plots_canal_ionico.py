import matplotlib.pyplot as plt
import numpy as np

Data1 = np.genfromtxt("Canal_ionico.txt")
Data2 = np.genfromtxt("Canal_ionico1.txt")

X1 = Data1[:,0]		
Y1 = Data1[:,1]

X2 = Data2[:,0]
Y2 = Data2[:,1]

N = 1000


def MinDist_1(X, Y):	#La minima distancia entre un punto de prueba y un punto del Set de Datos, implica el maximo radio en ese punto
	Dist_1 = []				
	R_1 = 0.0

	for i in range(len(X1)):
		Dist_1.append(np.sqrt(((X-X1[i])**2+(Y-Y1[i])**2)))		#Distancia entre un punto de prueba y las coordenadas de los puntos
   	for i in range(len(X1)):
		if Dist_1[i] < Dist_1[0]:								#En la posicion 0 ahora voy a tener siempre la minima distancia (El mejor R)
			Dist_1[0] = Dist_1[i]
			R_1 = Dist_1[0]
	return R_1													#Esta funcion me retorna el mejor radio en un punto de prueba dado X,Y


X_W1 = [5]			#Al visualizar los datos hago un "guess" del punto candidato...esto situa el punto dentro del poro
Y_W1 = [5]
R_init1 = MinDist_1(X_W1[0], Y_W1[0])
R_W1 = [R_init1]


for i in range(N):
	X_P1 = np.random.normal(X_W1[i], 0.1) 
	Y_P1 = np.random.normal(Y_W1[i], 0.1)
	R_init1 = MinDist_1(X_W1[i], Y_W1[i])
	R_P1 = MinDist_1(X_P1, Y_P1)
    
	Alpha1 = R_P1/R_init1

	if(Alpha1>=1.0):
		X_W1 = np.append(X_W1, X_P1)
		Y_W1 = np.append(Y_W1, Y_P1)
		R_W1 = np.append(R_W1, R_P1)
	else:
		Beta1 = np.random.normal()
		if(Beta1<=Alpha1):
			X_W1 = np.append(X_W1, X_P1)
			Y_W1 = np.append(Y_W1, Y_P1)
			R_W1 = np.append(R_W1, R_P1)
		else:
			X_W1 = np.append(X_W1, X_W1[i])
			Y_W1 = np.append(Y_W1, Y_W1[i])
			R_W1 = np.append(R_W1, R_init1)

Mejor_Radio1 = np.argmax(R_W1)
Best_X1 = X_W1[Mejor_Radio1]
Best_Y1 = Y_W1[Mejor_Radio1]

RadioMaximo1 = MinDist_1(Best_X1, Best_Y1)

#--------------------------------------------------------------------------------------------------------------------------------------------
def MinDist_2(X, Y):	#La minima distancia entre un punto de prueba y un punto del Set de Datos, implica el maximo radio en ese punto
	Dist_2 = []				
	R_2 = 0.0

	for i in range(len(X2)):
		Dist_2.append(np.sqrt(((X-X2[i])**2+(Y-Y2[i])**2)))		#Distancia entre un punto de prueba y las coordenadas de los puntos
   	for i in range(len(X2)):
		if Dist_2[i] < Dist_2[0]:								#En la posicion 0 ahora voy a tener siempre la minima distancia (El mejor R)
			Dist_2[0] = Dist_2[i]
			R_2 = Dist_2[0]
	return R_2													#Esta funcion me retorna el mejor radio en un punto de prueba dado X,Y


X_W2 = [5]			#Al visualizar los datos hago un "guess" del punto candidato...esto situa el punto dentro del poro
Y_W2 = [5]
R_init2 = MinDist_2(X_W2[0], Y_W2[0])
R_W2 = [R_init2]


for i in range(N):
	X_P2 = np.random.normal(X_W2[i], 0.1) 
	Y_P2 = np.random.normal(Y_W2[i], 0.1)
	R_init2 = MinDist_2(X_W2[i], Y_W2[i])
	R_P2 = MinDist_2(X_P2, Y_P2)
    
	Alpha2 = R_P2/R_init2

	if(Alpha2>=1.0):
		X_W2 = np.append(X_W2, X_P2)
		Y_W2 = np.append(Y_W2, Y_P2)
		R_W2 = np.append(R_W2, R_P2)
	else:
		Beta2 = np.random.normal()
		if(Beta2<=Alpha2):
			X_W2 = np.append(X_W2, X_P2)
			Y_W2 = np.append(Y_W2, Y_P2)
			R_W2 = np.append(R_W2, R_P2)
		else:
			X_W2 = np.append(X_W2, X_W2[i])
			Y_W2 = np.append(Y_W2, Y_W2[i])
			R_W2 = np.append(R_W2, R_init2)

Mejor_Radio2 = np.argmax(R_W2)
Best_X2 = X_W2[Mejor_Radio2]
Best_Y2 = Y_W2[Mejor_Radio2]

RadioMaximo2 = MinDist_2(Best_X2, Best_Y2)

#-------------CIRCULOS---------------------


#Canal 1 RadioMaximo
plt.figure()
plt.title("Canal Ionico 1")
#plt.scatter(X_W1, Y_W1, color="dodgerblue")
plt.ylim(-10,20)
plt.xlim(-15,25)
plt.scatter(X1, Y1, s=15)
plt.scatter(Best_X1, Best_Y1, color = "Black", s=20, label = "Radio Maximo = %f, X= %f, Y= %f" % (RadioMaximo1, Best_X1, Best_Y1))
Angle1 = np.linspace(0, 2*np.pi, 100)
CircleX1 = (RadioMaximo1-0.5)*np.cos(Angle1)+Best_X1
CircleY1 = (RadioMaximo1-0.5)*np.sin(Angle1)+Best_Y1
plt.legend()
plt.plot(CircleX1, CircleY1, color = "Green")
plt.savefig("RMC1.png")

#Canal 2 RadioMaximo
plt.figure()
plt.title("Canal Ionico 2")
#plt.scatter(X_W2, Y_W2, color="dodgerblue")
plt.ylim(-10,20)
plt.xlim(-15,25)
plt.scatter(X2, Y2, s=15)
plt.scatter(Best_X2, Best_Y2, color = "Black", s=20, label = "Radio Maximo = %f, X= %f, Y= %f" % (RadioMaximo2, Best_X2, Best_Y2))
Angle2 = np.linspace(0, 2*np.pi, 100)
CircleX2 = (RadioMaximo2-0.5)*np.cos(Angle2)+Best_X2
CircleY2 = (RadioMaximo2-0.5)*np.sin(Angle2)+Best_Y2
plt.legend()
plt.plot(CircleX2, CircleY2, color = "Green")
plt.savefig("RMC2.png")

#-------------HISTOGRAMAS---------------------

#Histograma X1
plt.figure()
plt.hist(X_W1, 30, normed=True, color ="darkorange")
plt.ylabel("Frecuencia", fontsize = 15)
plt.xlabel("Valores de X", fontsize = 15)
plt.title("Histograma para valores de X en Canal 1", fontsize = 18)
plt.savefig("HX1.png")

#Histograma Y1
plt.figure()
plt.hist(Y_W1, 30, normed=True, color ="darkblue")
plt.ylabel("Frecuencia", fontsize = 15)
plt.xlabel("Valores de Y", fontsize = 15)
plt.title("Histograma para valores de Y en Canal 1", fontsize = 18)
plt.savefig("HY1.png")

#Histograma X2
plt.figure()
plt.hist(X_W2, 30, normed=True, color ="darkorange")
plt.ylabel("Frecuencia", fontsize = 15)
plt.xlabel("Valores de X", fontsize = 15)
plt.title("Histograma para valores de X en Canal 2", fontsize = 18)
plt.savefig("HX2.png")

#Histograma Y2
plt.figure()
plt.hist(Y_W2, 30, normed=True, color ="darkblue")
plt.ylabel("Frecuencia", fontsize = 15)
plt.xlabel("Valores de Y", fontsize = 15)
plt.title("Histograma para valores de Y en Canal 2", fontsize = 18)
plt.savefig("HY2.png")

