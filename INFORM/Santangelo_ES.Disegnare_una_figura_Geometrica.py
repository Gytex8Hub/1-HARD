import turtle
v=turtle.Pen()
nlati=int(input('inserisci il numero di lati'))
llati=int(input('inserisci la lunghezza del lato'))

tot_ang=(nlati-2)*180
ang_est=180-(tot_ang//nlati)

for i in range(nlati):
    v.forward(llati)
    v.left(ang_est)
    
    
