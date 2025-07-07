def split_and_join(line):
    line = line.split(" ") #Separa por caracter y devuelve una lista.
    line_2 = "-".join(line) #Une lista en un string separado por un caracter.

    print (f"Hello {line}, welcome to python!") # f-strings son usados para insertar variables en el strings.

    def mutate_string(string, position, character):
        s_list = list(string)
        s_list[position] = character
        s_string = ''.join(s_list) # Join tambien permite convertir listas en strings de esta forma.
        return s_string

    return line_2