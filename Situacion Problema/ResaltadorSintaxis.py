import webbrowser
import re
'''
Este programa permite leer un archvivo con codigo Scheme
y devolver un archivo HTML con los lexemas resaltados.
Complejidad General del proceso: O(n)
Autor: Joel Isaí Ramos Hernández
Matrícula: A01245083
Ultima modificación: 12 de marzo de 2021
'''
# Aquí escriba el nombre del archivo TXT con el codigo de entrada
nombreArchivoTXT = 'codigo'
tipoArchivo = 'txt'
# Aquí escriba el nombre que quiere que tenga el archivo HTML de salida
nombreArchivoHTML = 'codigoResaltado'
# Si quiere que automaticamente se abra el archivo HTML, esciba la ruta/direccion en donde esta este archivo dentro de su computadora 
ruta = 'D:/Users/Documents/Escuela/4toSemestre/Lenguajes Programacion/SituacionProblema/'


# Funcion para meter el lexema dentro de un span con su token como clase
# Complejidad O(1)
def agregarToken(textoHTML, token, lexema):
    textoHTML += "<span class=\""
    textoHTML += token
    textoHTML += "\">"
    textoHTML += lexema
    textoHTML += "</span>"
    return textoHTML


# Funcion para reconocer un lexema por medio de su expresion regular
# Complejidad O(1)
def buscarLexema(regex, lexema):
    try:
        return re.search(regex, lexema).group() == lexema
    except:
        return False


# Listas y expresiones regualres para reconocer lexemas
operadoresLogicos = ["<", ">", "=", "<=", ">=", "<>", "'"]
operadoresNumericos = ["+", "-", "*", "/"]
palabrasReservadas = ["define", "lambda", "if", "cond", "else", "true", "false", "nil", "car", "cdr", "cons", "list", "apply", "map", "let", "begin", "null?", "eq?", "set!"]
regexEntero = r'(-|)(\d)+'
regexDecimal = r'(-|)(\d+)\.\d+([eE](-|)\d+|)'
regexIndentificador = r'[^\(\)\[\]\{\};,\'\"#\\\s]+'


# Expesion regular para reconocer y separar todos lexemas 
expresionRegular = r'(\B(\+|-|\*|/|<=|>=|<>|=|<|>|\')\B)|((-|)(\d+)\.\d+([eE](-|)\d+|)(\b))|((-|)(\d)+(\b))|([^\(\)\[\]\{\};,\'\"#\\\s]+)|(;[^\n]*)|\(|\)| |\n|[^ \n]+'


# Leer el codigo y guardarlo en una variable
archivoTXT = open( nombreArchivoTXT + '.' + tipoArchivo, 'r')
codigo = archivoTXT.read()
archivoTXT.close()


# Iniciar el texto HTML
textoHTML = """<html>
<head></head>
    <body>
        <p>

"""


#Iniciar el patron de la expresion regular general 
patron = re.compile(expresionRegular)

lexemas = patron.finditer(codigo)
# Complejidad O(n)
for lexema in lexemas: 
    lex = lexema.group()

    # Debug: Imprimir cada lexema individual en terminal o consola
    # print(lex)
    
    if lex in operadoresNumericos:
        textoHTML = agregarToken(textoHTML, "Operador Numerico", lex)
    elif lex in operadoresLogicos:
        textoHTML = agregarToken(textoHTML, "Operador Logico", lex)
    elif lex in palabrasReservadas:
        textoHTML = agregarToken(textoHTML, "PalabraReservada", lex)
    elif lex[0] == ";":
        textoHTML = agregarToken(textoHTML, "Comentario", lex)
    elif lex == "(":
        textoHTML = agregarToken(textoHTML, "Parentesis Abierto", lex)
    elif lex == ")":
        textoHTML = agregarToken(textoHTML, "Parentesis Cerrado", lex)
    elif lex == ' ':
        # textoHTML += lex
        textoHTML += "&nbsp;"
    elif lex == '\n':
        textoHTML += "\n<br>\n"
    elif buscarLexema(regexDecimal, lex):
        textoHTML = agregarToken(textoHTML, "Numero Decimal", lex)
    elif buscarLexema(regexEntero, lex):
        textoHTML = agregarToken(textoHTML, "Numero Entero", lex)
    elif buscarLexema(regexIndentificador, lex):
        textoHTML = agregarToken(textoHTML, "Identificador", lex)
    else:
        textoHTML = agregarToken(textoHTML, "Error", lex)


# Cerrar el texto HTML e incluir el CSS
textoHTML += """

        </p>
    <style>
        p {
            font-size: 18px;
            line-height: 30px;
            letter-spacing: 1px;
            font-family: "Courier New";
        }

        .PalabraReservada {
            color: purple;
            font-weight: bolder;
        }

        .Operador {
            color:rgb(245, 0, 0);
        }

        .Parentesis{
            color:black;
        }

        .Identificador {
            color: blue;
            font-weight:bold;
        }

        .Comentario{
            color: rgb(26, 122, 2);
            font-style: italic;
            font-weight: 500;
        }

        .Numero {
            color:rgb(7, 170, 211);
        }

        .Error {
            background-color: red;
        }
    </style>
    </body>
</html>"""


# Crear y llenar el archivo HTML con el nuevo codigo
archivoHTML = open(nombreArchivoHTML + '.html','w')
archivoHTML.write(textoHTML)
archivoHTML.close()


# Debug: Imprimir en consola o terminal
# print("begin\n" + textoHTML +"\nend")


# Abrir el HTML en el buscador 
direccionArchivo = ruta + nombreArchivoHTML + '.html'
webbrowser.open_new_tab(direccionArchivo)



''' Expresiones Regulares (Regex) individualmente'''
# Operadores
# \B(\+|-|\*|/|<=|>=|<>|=|<|>|\')\B

# Numero Entero 
# (-|)(\d)+(\b)

# Numero Decimal
# (-|)(\d+)\.\d+([eE](-|)\d+|)(\b)

# Commentario
# ;[^\n]*

# Identificador
# \b[^\(\)\[\]\{\};,\'\"#\\\s]+(\b)