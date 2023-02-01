/*
    Name:Santangelo_Es.CALCOLATRICE
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
	int somma=0;
	int sott=0;
	int molt=0;
	float div=0;
	int n1=0;
	int n2=0;
	int variabile;
//4. input
	
	
do { 
	cout<<"se premi 1, esegue la somma\n";
	cout<<"se premi 2, esegue le sottrazione\n";
 	cout<<"se premi 3, esegue la moltiplicazione\n";
	cout<<"se premi 4, esegue la divisione\n";
	cout<<"se premi 5, esce dal programma\n";
		
	cin>>variabile;

//5. logica - operazioni - algoritmo

switch (variabile){

	case 1:
//istruzioni

cout<<"inserisci n1: ";
cin>>n1;
cout<<"inserisci n2: ";
cin>>n2;
somma=n1+n2;
cout<<"la somma dei due numeri e\' "<<somma;
n1=0;
n2=0;
cout<<"\n";
break;

	case 2:
//istruzioni

cout<<"inserisci n1: ";
cin>>n1;
cout<<"inserisci n2: ";
cin>>n2;
sott=n1-n2;
cout<<"la sottrazione tra i due numeri e\' "<<sott;
n1=0;
n2=0;
cout<<"\n";
break;

	case 3:
//istruzioni

cout<<"inserisci n1: ";
cin>>n1;
cout<<"inserisci n2: ";
cin>>n2;
molt=n1*n2;
cout<<"la moltiplicazione tra i due numeri e\' "<<molt;
n1=0;
n2=0;
cout<<"\n";
break;

	
	case 4:
//istruzioni

cout<<"inserisci n1: ";
cin>>n1;
cout<<"inserisci n2: ";
cin>>n2;
div=n1/n2;
cout<<"la divisione tra i due numeri e\' "<<div;
n1=0;
n2=0;
cout<<"\n";
break;
	
	
	case 5:
//istruzioni

cout<<"arrivederci e grazie";
cout<<"\n";
break;	

}
}while(variabile!=5); 	


//istruzioni

//6. output


//7. ritorno al sistema operativo
return 0;
//8. fine del programma
}
