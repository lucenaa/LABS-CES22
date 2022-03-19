import turtle


def draw_poly(t, n, sz):
    # Função que constrói um polígono de n lados, cada um com medida l
    for i in range(n):
        t.forward(sz)
        t.left(360/n)


pg = turtle.Screen()
pg.bgcolor("lightgreen")
pg.title("Questão 02")
ttg = turtle.Turtle()
ttg.pensize(4)
ttg.color("#F67280")

draw_poly(ttg, 8, 50)
pg.mainloop()