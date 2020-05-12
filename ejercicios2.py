numA = 2
numB = 6
numC = 8
suma = numA + numB
resta = numC - numA
division = numC / numA
multiplicacion = numB * numA
elevacion = numC ** numA
modulo = numC % numA
print("suma de 2 + 8=",suma,"resta de 8 - 2=",resta,
    "division de 8 / 2=",division,"multiplicacin de 6 * 2=",multiplicacion,"elevacion de 8^2=",elevacion,"modulo de 8 entre 2=",modulo)
operaCombinada = numB*(numB +((numA**numC)-(numA /(numC * numA))))
numA = operaCombinada
operaCombinada = numC
numC = operaCombinada
print(numA)