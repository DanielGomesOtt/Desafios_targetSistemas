n = 34
sequencia = list()
ultimo = 1
penultimo = 1

if (n == 1) or (n == 2):
    sequencia.append("1")
else:
    contador = 3
    while contador <= n:
        valor = ultimo + penultimo
        penultimo = ultimo
        ultimo = valor
        contador = contador + 1
        sequencia.append(valor)
    

if n in sequencia:
    print(f"O valor {n} pertence a sequencia de Fibonacci")
else:
    print(f"O valor {n} nao pertence a sequencia de Fibonacci")
