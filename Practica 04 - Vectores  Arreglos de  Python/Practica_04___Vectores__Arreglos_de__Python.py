maxf = 3
maxc = 5
a = [[0.0] * maxc for _ in range(maxf)]


print("Asigna los numeros para rellenar la matriz de 3x5:")
for f in range(maxf):
    for c in range(maxc):
        a[f][c] = float(input())



print("La matriz resultante de 3x5 es:")
for f in range(maxf):
    for c in range(maxc):
        print(a[f][c], end=" ") 
    print()
