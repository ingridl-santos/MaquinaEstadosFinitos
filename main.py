'''
  Aluna: Ingrid Lima dos Santos
  Trabalho 1 - Maquina de Estados Finitos

  Para obter os pontos relativos a este trabalho, você deverá cirar um programa, utilizando a linguagem Python, C, ou C++. Este programa, quando executado irá determinar se uma string de entrada faz parte da linguagem L definida por 𝐿 = {𝑥 | 𝑥 ∈ {𝑎,𝑏}∗ 𝑒 𝑐𝑎𝑑𝑎 𝑎 𝑒𝑚 𝑥 é 𝑠𝑒𝑔𝑢𝑖𝑑𝑜 𝑝𝑜𝑟 𝑝𝑒𝑙𝑜 𝑚𝑒𝑛𝑜𝑠 𝑑𝑜𝑖𝑠 𝑏} segundo o alfabeto Σ={𝑎,𝑏,𝑐}.
  O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt) contendo várias strings. A primeira linha do arquivo indica quantas strings estão no arquivo de texto de entrada. As linhas subsequentes contém uma string por linha. A seguir está um exemplo das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
        3 
        abbaba 
        abababb 
        bbabbaaab
  Neste exemplo temos 3 strings de entrada. O número de strings em cada arquivo será representado por um número inteiro positivo. A resposta do seu programa deverá conter uma, e somente uma linha de saída para cada string. Estas linhas conterão a string de entrada e o resultado da validação conforme o formato indicado a seguir:  
        abbaba: não pertence.
  A saída poderá ser enviada para um arquivo de textos, ou para o terminal padrão e será composta de uma linha de saída por string de entrada. No caso do exemplo, teremos 3 linhas de saída.
  Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada contendo um número diferente de strings diferentes. Os arquivos de entrada criados para os seus testes devem estar disponíveis tanto no ambiente repl.it quanto no ambiente Github. Observer que o professor irá testar seu programa com os arquivos de testes que você criar e com, no mínimo um arquivo de testes criado pelo próprio professor.

 Modo de execução:

 python main.py [nome arquivo teste]
'''
import sys

filename = sys.argv[1]
archive = open(filename)
lines = archive.readline()
alphabet = ['a', 'b', 'c']

for size in range(int(lines)):
    np = False
    str = archive.readline().strip('\n')

    for char in range(len(str)):
        if (str[char] not in alphabet):
            np = True

        if (str[char] == 'a' and (char >= len(str) - 2 or str[char + 1] != 'b'
                                  or str[char + 2] != 'b')):
            np = True

    if (np):
        print(str + ': não pertence')
    else:
        print(str + ': pertence')
