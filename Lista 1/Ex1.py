import turtle


def draw_poly(t, n, sz):
    # Função que constrói um polígono de n lados, cada um com medida l
    for i in range(n):
        t.forward(sz)
        t.left(360/n)


pg = turtle.Screen()
pg.bgcolor("lightgreen")
pg.title("Questão 01")
ttg = turtle.Turtle()
ttg.pensize(4)
ttg.color("#F67280")
qtde = 5

for i in range(qtde):
    draw_poly(ttg, 4, (i+1)*20)
    ttg.up()
    ttg.setposition(-(i+1)*20/2, -(i+1)*20/2)
    ttg.down()

pg.mainloop()