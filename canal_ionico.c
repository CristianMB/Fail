#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int Coordenadas(int i, int j);
float CalcularDistancia(float Xi, float Xf, float Yi, float Yf);


int i;					//Variables de Iteracion
int j;

int N = 100000;			//Cantidad de Iteraciones

float Puntos_C1[42][2];	//Coordenadas puntos de Canal_1 (Se sabe que son 42 datos por columna al realizar una inspeccion en Python)
float Puntos_C2[42][2];	//Coordenadas puntos de Canal_2

float RW_X1[N];			//Random Walk X1, Y1, R1
float RW_Y1[N];
float RW_R1[N];

float RW_X2[N];			//Random Walk X2, Y2, R2
float RW_Y2[N];
float RW_R2[N];

float Alpha1;
float Alpha2;
float Beta1;
float Beta2;
float r=1.0;

//-------------MAIN------------------------------------------------------------------

void main(void)
{
	FILE *Data1; 

	Data1 = fopen("Canal_ionico.txt", "r");

	for(i=1; i=42; i++)
	{
		fscanf(in, "%f\n", &Puntos_C1[i]);
	}
	fclose(Data1);

	RandomW_1 = fopen("RW1.txt", "w");
	fprintf(Data, "%f %f %f\n", RW_X1[][]);
}

//-------------FUNCIONES------------------------------------------------------------------

float CalcularDistancia(float Xi, float Xf, float Yi, float Yf)
{
	float Distancia = sqrt(((Xf-Xi)*(Xf-Xi))+((Yf-Yi)*(Yf-Yi)))-r;
	if(Distancia > r)
	{
		return Distancia;
	}
	else
	{
		return 0;
	}
}
