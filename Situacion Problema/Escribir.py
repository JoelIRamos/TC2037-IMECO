import webbrowser
operadoresLogicos = ["<", ">", "=", "<=", ">=", "<>", "'"]
operadoresNumericos = ["+", "-", "*", "/"]
palabrasReservadas = ["define", "lambda", "if", "cond", "else", "true", "false", "nil", "car", "cdr", "cons", "list", "apply", "map", "let", "begin", "null?", "eq?", "set!"]
def agregarToken(textoHTML, token, lexema):
    textoHTML += "<span class=\""
    textoHTML += token
    textoHTML += "\">"
    textoHTML += lexema
    textoHTML += "</span>"
    return textoHTML



# Leer el codigo y guardarlo en una variable
f = open('codigo.txt', 'r')
codigo = f.read()
codigo += "\n"

# Iniciar el texto html
textoHTML = ""

lenght = len(codigo)
for i in range(lenght):
    lexema = ""

    if lexema == "(":
        textoHTML = agregarToken(textoHTML, "Parentesis Abierto", lexema)
    elif lexema == ")":
        textoHTML = agregarToken(textoHTML, "Parentesis Cerrado", lexema)
    elif lexema in operadoresNumericos:
        textoHTML = agregarToken(textoHTML, "Operador Numerico", lexema)
    elif lexema in operadoresLogicos: 
        textoHTML = agregarToken(textoHTML, "Operador Logico", lexema)
    elif lexema in palabrasReservadas:
        textoHTML = agregarToken(textoHTML, "PalabraReservada", lexema)
    elif False :
        textoHTML = agregarToken(textoHTML, "Identificador", lexema)
    elif False:
        textoHTML = agregarToken(textoHTML, "Numero Entero", lexema)
    elif False:
        textoHTML = agregarToken(textoHTML, "Numero Decimal", lexema)
    elif lexema == " ":
        textoHTML += " "
    elif lexema == "\n":
        textoHTML += "\n<br>\n"
    else:
        pass
    print(codigo[i], end="")





# f = open('holamundo.html','w')

# mensaje = """<html>
# <head></head>
# <body><p>"""
# f.write(mensaje)
# mensaje = """
# Hola Mundo!
# """
# f.write(mensaje)
# mensaje = """
# </p></body>
# </html>
# """
# f.write(mensaje)


# f.close()

# nombreArchivo = 'D:/Users/Documents/Escuela/4toSemestre/Lenguajes Programacion/SituacionProblema/' + 'holamundo.html'
# webbrowser.open_new_tab(nombreArchivo)