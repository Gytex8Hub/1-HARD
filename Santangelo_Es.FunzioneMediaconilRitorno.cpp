/*
    Name:Santangelo_Es.FunzioneMediaconilRitorno
    Copyright:Colamonico-Chiarulli
    Author:Gianluigi Santangelo
    Date: 28/09/22 09:39
    Description: acquisisco ivalori della funzione media con una funzione acuasizione
*/


//1. includo le librerie
#include <iostream>
using namespace std;
//2. inizio il blocco main

double acquisizione(){
	
	double a;
	cout<<"inserisci valore";
	cin>>a;

return a;
}

double media(double a,double b){
	double m;
	m=(a+b)/2;
	return m;
}


int main(){
//3. dichiaro e inizializzo le variabili
double valoremedia;

double var1;
double var2;

var1 = acquisizione();
var2 =acquisizione();


valoremedia = media(var1,var2);
cout<<valoremedia;                                                                                                                                                                                                                                     


//4. input


//5. logica - operazioni - algoritmo


//6. output


//7. ritorno al sistema operativo
return 0;
//8. fine del programma
}
