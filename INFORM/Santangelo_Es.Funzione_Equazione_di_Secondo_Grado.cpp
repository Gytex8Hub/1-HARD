/*
    Name:Santangelo_Es.Funzione_Equazione_di_Secondo_Grado
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

double CalcolaDelta (double a,double bq,double c);
	
int main(){
//3. dichiaro e inizializzo le variabili
double a;
double b;
double c;
double esp;
double bq;

cout<<"inserisci valore a ";
cin>>a;
cout<<"inserisci valore b ";
cin>>b;
cout<<"inserisci valore c ";
cin>>c;
cout<<"inserisci l'esponente ";
cin>>esp;
bq = pow(b,esp);
cout<<" il calcolo del delta e\' "<< CalcolaDelta(a,bq,c)<<endl;
//4. input


//5. logica - operazioni - algoritmo


//6. output


//7. ritorno al sistema operativo
return 0;
//8. fine del programma
}

double CalcolaDelta (double a,double bq,double c){
	double delta;
	delta = bq-(4*a*c);
	return delta;

}
