/*
    Name:Santangelo_Es.Temperature_Puglia
    Copyright:Colamonico-Chiarulli
    Author:Gianluigi Santangelo
    Date: 28/09/22 09:39
    Description:
*/


//1. includo le librerie
#include <iostream>
#include <cmath>
using namespace std;
//2. inizio il blocco main

	
int main(){
//3. dichiaro e inizializzo le variabili

int i;
int lunghVet=0;
int vettore1[i];
int vettore2[i];

cout<<"inserisci la lunghezza del vettore";
cin>>lunghVet;

for(i=0;i<lunghVet;i++) {
	cout<<"inserisci il valore della temperatura del vettore 1,"<<i<<" : ";
	cin>>vettore1[i];
	}
	
for(i=0;i<lunghVet;i++) {
	cout<<"inserisci il valore della temperatura del vettore 2,"<<i<<": ";
	cin>>vettore2[i];
	}
	
//7. ritorno al sistema operativo
return 0;
//8. fine del programma
	
}
