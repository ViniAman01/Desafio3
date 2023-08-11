import numpy as np #Biblioteca numpy

try:
    m = int(input("Informe o número de linhas da matriz maior que 0: "))
    n = int(input("Informe o número de colunas da matriz maior que 0: "))
    exp = float(input("Informe o expoente da potência no intervalo [0,1]: "))
    assert exp >= 0 and exp <= 1 and m > 0 and n > 0 #O assert garante que o usúario não digitará valores inválidos

    matrix = np.random.randint(1,255,size=(m,n),dtype=np.uint8) #Aqui é gerado um array do numpy, com valor máximo até 255, dimensões mxn e do tipo inteiro de 8 bits
    print("\nMatriz de entrada:")
    print(matrix)
    print()

    matrix_pow = matrix**exp
    print("Matriz após potenciação:")
    print(matrix_pow)
    print()

    matrix_log10 = np.log10(matrix)
    print("Matriz após logaritmo na base 10:")
    print(matrix_log10)
    print()

    matrix_log2 = np.log2(matrix)
    print("Matriz após logaritmo na base 2:")
    print(matrix_log2)
    print()

    coordinates = np.array([[1,1],[-1,-1],[0,1],[0,-1],[1,0],[-1,0],[1,-1],[-1,1]]) #Aqui são as coordenadas para encontrar os elementos adjancentes
    min_std = -1
    element = -1
    index_element = []

    for aux_matrix in [matrix_pow,matrix_log10,matrix_log2]: #Analisamos as 3 matrizes 
        for i in range(m): #Indice para percorrer as linhas 
            for j in range(n): #Indice para percorrer as colunas
                sub_matrix = []; #Criamos uma submatriz para armazenar os valores adjancentes
                for cd in coordinates: #Usando os valores das coordenadas para fazer somas sobre os indices 
                    if i+cd[0] < m and j+cd[1] < n and i+cd[0] >= 0 and j+cd[1] >= 0: #Condições para garatir que não vamos sair do alcance da matriz
                       sub_matrix.append(aux_matrix[i+cd[0]][j+cd[1]]) #Adicionamos os valores adjancentes de cada elemento para a submatriz
                sub_matrix.append(aux_matrix[i][j]) #Adicionamos o próprio elemento para a submatriz
                if i == 0 and j == 0 and min_std == -1:
                    min_std = np.std(np.array(sub_matrix,dtype=np.float64))
                    element = aux_matrix[i][j]
                    index_element = [i,j]
                current_std = np.std(np.array(sub_matrix,dtype=np.float64))
                if current_std < min_std:
                    min_std = current_std
                    element = aux_matrix[i][j]
                    index_element = [i,j]

    print(f'Menor desvio padrão dos elementos adjacentes foi do elemento {element}, posição [{index_element[0]},{index_element[1]}]: {min_std}')
except AssertionError: #Caso o usúario tenha digitado um valor fora de algum intervalo, a mensagem de erro é apresentada.
    print("Você digitou um valor fora do intervalo.")
