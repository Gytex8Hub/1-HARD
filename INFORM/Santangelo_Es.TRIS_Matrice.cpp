/*
    Name:Santangelo_Es.TRIS_Matrice
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
int righe=0;
int colonne=0;
int matrice[righe][colonne];
int nr;
int nc;

//4. input
cout<<"inserisci le righe della matrice: ";
cin>>righe;
cout<<"inserisci le colonne della matrice: ";
cin>>colonne;

//5. logica - operazioni - algoritmo
colonne=colonne-1;
righe=righe-1;
for(nr=0;nr<=righe;nr++) {
	nc=0;
	for(nc=0;nc<=colonne;nc++) {
		cout<<"inserisci il valore della matrice "<<nr<<nc<<":";
		cin>>matrice[nr][nc];
}
}


for(nr=0;nr<=righe;nr++) {
	nc=0;
	cout<<endl;
	for(nc=0;nc<=colonne;nc++) {
		cout<<matrice[nr][nc]<<" ";
}
}


//6. output


//7. ritorno al sistema operativo
return 0;
//8. fine del programma
}
