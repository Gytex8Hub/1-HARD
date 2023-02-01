/*
    Name:Santangelo_Es.Sblocco_Cellulare
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
	int lunghVet=4;
	int vettore_0[i];
	int vettore_1[i];
	int vettore_accesso[i];
	int c=0;
	int variabile;
	int ne=0;

//4. input

do { 
	cout<<"se premi 1, imposti un pin\n";
	cout<<"se premi 2, accedi al dispositivo\n";
 	cout<<"se premi 3, esca dal programma\n";
 
	cin>>variabile;

//5. logica - operazioni - algoritmo

switch (variabile){

	case 1:
//istruzioni

while(c==0){
	
	c=1;
	cout<<"Il telefono non e\' protetto da un pin, per la tua sicurezza inseriscilo di quattro cifre : ";
	for(i=0;i<lunghVet;i++) {
	cin>>vettore_0[i];
	}
    cout<<"perfavore reinserisci il pin : ";
	for(i=0;i<lunghVet;i++) {
	cin>>vettore_1[i];
	}
	i=0;
	lunghVet=lunghVet-1;
	while(i<=lunghVet && c==1) {
		if(vettore_1[i]!=vettore_0[i]) {
			cout<<"Errore!, inserire nuovamente il pin"<<endl;
			c=0;
	
}
	i=i+1;
}
lunghVet=lunghVet+1;
}
	cout<<"perfetto, ora il telefono e\' protetto da un pin!";
c=1;	
cout<<"\n";
break;	
	


	case 2:
//istruzioni

while(c==1 && ne<=2){
    
    c=0;
	cout<<"prima di accedere al dispositivo inserire il pin in uso ";
	for(i=0;i<lunghVet;i++) {
	cin>>vettore_accesso[i];
	}
	i=0;
	lunghVet=lunghVet-1;
	while(i<=lunghVet && c==0) {
		if(vettore_accesso[i]!=vettore_1[i]) {
			cout<<"Errore!, inserire nuovamente il pin"<<endl;
			c=1;
			ne=ne+1;
}
	

i=i+1;
}
lunghVet=lunghVet+1;
}
		
	if(ne>=3)
		cout<<"telefono bloccato";
	if(c==0) {
		cout<<"perfetto, hai accesso al dispositivo";
}
	
cout<<"\n";
break;	

	
	
	case 3:
//istruzioni

cout<<"arrivederci e grazie";
cout<<"\n";
break;	

}
}while(variabile!=3); 	


	



//6. output


//7. ritorno al sistema operativo
return 0;
//8. fine del programma
}
