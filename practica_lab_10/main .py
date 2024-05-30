def contar_rutas(laberinto):
    m = len(laberinto)
    n = len(laberinto[0])

    if laberinto[0][0] == 1 or laberinto[m-1][n-1] == 1:
        return 0

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            if laberinto[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]

    return dp[m-1][n-1]

# Ejemplo de uso
laberinto = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

print(f"Rutas posibles: {contar_rutas(laberinto)}")