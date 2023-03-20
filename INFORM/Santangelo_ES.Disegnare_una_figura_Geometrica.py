import turtle
v=turtle.Pen()
nlati=int(input('inserisci il numero di lati'))

tot_ang=(nlati-2)*180
print(tot_ang)
ang_est=180-(tot_ang//nlati)

for i in range(nlati):
    v.forward(100)
    v.left(ang_est)
    
    
