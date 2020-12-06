import re  # importacion expresion regular para el codigo, 
path = "archivo.txt"
codigo = "codigobasico.txt"

# manejo de error para si no se encuentra el archivo
try:
    archivo1 = open(codigo, 'r')
except:
    # por si no se encuentra el archivo
    print("No se puede encontrar el archivo codigo")
    quit()

muestracodigo = ""

for linea1 in archivo1:
    muestracodigo += linea1


try:
    archivo = open(path, 'r')
except:
    print("El archivo no se encuentra")
    quit()

texto = ""

for linea in archivo:
    texto += linea

patronVARIABLES = r'(\b[A-Za-z0-9-_]+\s*[=])+'

resultadoVARIABLES = re.findall(patronVARIABLES, muestracodigo)
print("Las variables que estan declaradas son estas: ",
      resultadoVARIABLES)  
print("")  

#Enteros y decimales. 2.7, 3.1416, 0.2, etc.
# Entero
patronENTERO = r'[+,-]?[0-9]+'
resultadoENTERO = re.findall(patronENTERO, texto)
print("Los numeros enteros del archivo son estos: ", resultadoENTERO)
print("")

# Decimal
patronDECIMAL = r'[+,-]?[[0-9]*[.]]?[0-9]+'
resultadoDECIMAL = re.findall(patronDECIMAL, texto)

print("Los numeros decimales del archivo son estos: ", resultadoDECIMAL)
print("")

# Operadores aritméticos (suma, resta)

patronARITMETICO = r'[\d+]+\s*[\+|\-|\*|\/]+\s*[\d+]+'
resultadoARITMETICO = re.findall(patronARITMETICO, texto)
print("Los operadores aritmeticos del archivo son: ", resultadoARITMETICO)
print("")

# Operadores relacionales. (mayor, menor, igual, diferente, etc.)
patronRELACIONAL = r'([A-Za-z0-9|a-z0-9]+\s*[|<|>|!=|<=|>=]=+\s*[A-Za-z0-9|a-z0-9])+'
resultadoRELACIONAL = re.findall(patronRELACIONAL, texto)
print("Los operadores relacionales identificados son: ", resultadoRELACIONAL)
print("")

# Palabras reservadas.
PatronRESERVADAS = r'\b(False|def|if|raise|None|del|import|return|True|elif|in|try|and|else|is|while|as|except|lambda|with|assert|finally|nonlocal|yield|break|for|not|class|from|or|continue|global|pass\s)+|\s[:]+'
resultadoRESERVADAS = re.findall(PatronRESERVADAS, muestracodigo)
print("Las palabras reservadas son estos: ", resultadoRESERVADAS)
print("")
fin
