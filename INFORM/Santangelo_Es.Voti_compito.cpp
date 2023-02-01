/*
    Name:Santangelo_Es.Voti_compito
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
	int lunghVet;
	int vettore[i];
	int num_s=0;
	int num_i=0;
	char V;
	char F;
	bool suffmagginsu=V;


//4. input
cout<<"inserisci la lunghezza del vettore";
cin>>lunghVet;
for(i=0;i<lunghVet;i++) {
	cout<<"inserisci il voto dell'alunno '"<<i<<" : ";
	cin>>vettore[i];
	}

//5. logica - operazioni - algoritmo
for(i=0;i<lunghVet;i++) {
if(vettore[i]>=6) {
num_s=num_s+1;
}
else{
	num_i=num_i+1;
}
}

if(num_s>num_i) {
suffmagginsu=V;
cout<<suffmagginsu;
}
else{
suffmagginsu=F;
cout<<suffmagginsu;
}



//6. output
cout<<"il numero dei voti sufficenti e\': "<<num_s<<endl;
cout<<"il numero dei voti insufficenti e\': "<<num_i;
//7. ritorno al sistema operativo
return 0;
//8. fine del programma
}
