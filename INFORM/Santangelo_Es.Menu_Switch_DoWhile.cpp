/*
    Name:Santangelo_Es.Menu_Switch_DoWhile
    Copyright:Colamonico-Chiarulli
    Author:Gianluigi Santangelo
    Date: 28/09/22 09:39
    Description:
*/


//1. includo le librerie
#include <iostream>
using namespace std;

//2. inizio il blocco main

int main(){
	
//3. dichiaro e inizializzo le variabili
    
	int i;
	int lunghVet=0;
	float somma=0;
	int vettore[i];
	int variabile;
	
	//4. input

do { 
	cout<<"se premi 1, inserisci il vettore\n";
	cout<<"se premi 2, stampi a video il vettore\n";
	cout<<"se premi 3, stampi il vettore ordinato al contrario\n";
	cout<<"se premi 4, esci dal programma\n\n";

	cin>>variabile;
	
//5. logica - operazioni - algoritmo
switch (variabile){

//istruzioni	
	case 1:
//istruzioni
    
    cout<<"\n";


break;	

	case 2:
//istruzioni
    cout<<"STAMPA:";
    cout<<"\n";

break; 
	
	case 3:
//istruzioni
    cout<<"STAMPA AL CONTRARIO:";
	    cout<<"\n";
break;	
	
	case 4:
//istruzioni
cout<<"arrivederci e grazie";
break;

}
} while(variabile!=4); 	

//7. ritorno al sistema operativo
return 0;
//8. fine del programma
}
