def split_and_join(line):
    line = line.split(" ") #Separa por caracter y devuelve una lista.
    line_2 = "-".join(line) #Une lista en un string separado por un caracter.

    print (f"Hello {line}, welcome to python!") # f-strings son usados para insertar variables en el strings.

    return line_2