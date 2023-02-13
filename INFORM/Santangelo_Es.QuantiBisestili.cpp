/*
    Name:Santangelo_Es.QuantiBisestili
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

bool IsBisestile(int anno);
	
int main(){
//3. dichiaro e inizializzo le variabili
int anno;
//4. input

cout<<"inserisci l'anno epr intero";
cin>>anno;
//5. logica - operazioni - algoritmo
cout<<IsBisestile(anno);

//6. output


//7. ritorno al sistema operativo
return 0;
//8. fine del programma
}
bool IsBisestile(int anno){
	bool annob;
	string vero;
	if(anno%100==0 & anno%400==0) {
		annob=vero;
}

	
	return annob;
	
}
