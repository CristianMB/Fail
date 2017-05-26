import matplotlib.pyplot as plt
import numpy as np

Datos = np.genfromtxt("CircuitoRC.txt")		#Datos Q(t)

t = Datos[:,0]				#Columna de valores de tiempo del circuito
Q = Datos[:,1]				#Informacion de la Carga Qmax=CV [Datos observados o "Real"]


V0 = 10						#Valor del potencial	
N = 15000						#Cantidad de Iteraciones

def q(R, C, t):				#La carga q(t) esta dada por la carga en el condensador: Qmax=CV [Mi modelo o "Model"]
	return C*V0*(1-np.exp(-t/(R*C)))


#------------------------------------------------------------------------------------------------
#Se quieren estimar parametros para R y C


def LikeliHood(Real, Model):						#En este caso "Real" seran los datos de Q y "Model" sera la funcion q(t)
	Chi_S = (1.0/2.0)*sum(((Real-Model)/100)**2)	#A diferencia del ejemplo del repositorio, aca elegimos un sigma distinto de 1	
	return np.exp(-Chi_S)



R_W = [0]			#Estas caminatas definiran los mejores parametros de "Mi Modelo", las inicializo en cualquier numero (en este caso 0)
C_W = [0]			#Aca se guardan  los pasos al realizar las caminatas, son los "Walk" = w para "C"=Capacitor y "R"=Resistencia
L_init = LikeliHood(Q, q(R_W[0], C_W[0], t))				#Inicializacion del LikeliHood
L_W = [LikeliHood(Q,L_init)]					#L_W = Likelihood_Walk



for i in range(N):
	R_P = np.random.normal(R_W[i], 0.1)		#R_P y C_P son " _Prime" (Son los nuevos valores actuales)	
	C_P = np.random.normal(C_W[i], 0.1)			
	L_P = LikeliHood(Q, q(R_P, C_P, t))	#Actualizo el LikeliHood con los Nuevos Valores Actuales de R y C

	Alpha = L_P/L_W[i]					#No hay problemas en L_W[0] pues la exponencial (e^-Chi_S) nunca se hace 0			
	
	if(Alpha>=1):						#Si el "parecimiento" es mayor "ahora" entonces agregar a la caminata los primados
		R_W = np.append(R_W, R_P)
		C_W = np.append(C_W, C_P)
		L_W = np.append(L_W, L_P)
	else:
		Beta = np.random.random()		#Una segunda decision aleatoria en caso de que la Condicion sobre Alpha no se cumpla
		if(Beta<=Alpha):		
			R_W = np.append(R_W, R_P)
			C_W = np.append(C_W, C_P)
			L_W = np.append(L_W, L_P)
		else:	
			R_W = np.append(R_W, R_W[i])
			C_W = np.append(C_W, C_W[i])
			L_W = np.append(L_W, L_W[i])	#A diferencia del elemplo no dejo el inicial sino el ultimo



Mejor_Ajuste = np.argmax(L_W)	#El mayor LikeliHood es el mejor ajuste
Best_R = R_W[Mejor_Ajuste]		
Best_C = C_W[Mejor_Ajuste]

Q_max =  V0*Best_C

print Best_R
print Best_C
print Q_max


#---------------------------------------------------------------------------------------------------------------------
#Graficas de Resultados:

#R vs Verosimilitud
plt.figure()
plt.scatter(R_W, -np.log(L_W), color = "darkgreen")
plt.ylabel("-ln(LikeliHood)", fontsize = 15)
plt.xlabel("Valores de R[Ohm]", fontsize = 15)
plt.title("Verosimilitud vs Valores de R", fontsize = 18)
plt.savefig("VSR.png")

#C vs Verosimilitud
plt.figure()
plt.scatter(C_W, -np.log(L_W), color = "darkred")
plt.ylabel("-ln(LikeliHood)", fontsize = 15)
plt.xlabel("Valores de C[F]", fontsize = 15)
plt.title("Verosimilitud vs Valores de C", fontsize = 18)
plt.savefig("VSC.png")

#Histograma para R
plt.figure()
plt.hist(R_W, 30, normed=True, color ="darkgreen")
plt.ylabel("Frecuencia", fontsize = 15)
plt.xlabel("Valores de R", fontsize = 15)
plt.title("Histograma para valores de R", fontsize = 18)
plt.savefig("HR.png")

#Histograma para C
plt.figure()
plt.hist(C_W, 30, normed=True, color ="darkred")
plt.ylabel("Frecuencia", fontsize = 15)
plt.xlabel("Valores de C", fontsize = 15)
plt.title("Histograma para valores de C", fontsize = 18)
plt.savefig("HC.png")

#Mejor Ajuste
plt.figure()
plt.plot(t, Q, color="dodgerblue", linewidth = 2, label = "Datos Observados")
plt.plot(t, q(Best_R, Best_C, t), color="Black", linewidth = 2, label="R = %f y C= %f" % (Best_R, Best_C))
plt.ylabel("Carga [C]", fontsize = 15)
plt.xlabel("tiempo [s]", fontsize = 15)
plt.title("Mejor Ajuste", fontsize = 18)
plt.legend(loc="best")
plt.savefig("MA.png")
