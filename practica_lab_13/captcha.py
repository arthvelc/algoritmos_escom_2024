import random
import math
import matplotlib.pyplot as plt

def generate_triangle_coordinates():
    # Vértices del triángulo equilátero
    V1 = (0, 0)
    V2 = (1, 0)
    V3 = (0.5, math.sqrt(3) / 2)
    return V1, V2, V3

def midpoint(P, V):
    return ((P[0] + V[0]) / 2, (P[1] + V[1]) / 2)

def generate_captcha_points(iterations=100):
    V1, V2, V3 = generate_triangle_coordinates()
    vertices = [V1, V2, V3]
    
    # Punto inicial aleatorio
    P = (random.uniform(0, 1), random.uniform(0, 1))
    points = [P]
    
    for _ in range(iterations):
        V = random.choice(vertices)
        P = midpoint(P, V)
        points.append(P)
    
    return points

def save_points_to_file(points, filename="captcha_points.txt"):
    with open(filename, "w") as file:
        for point in points:
            file.write(f"{point[0]} {point[1]}\n")

def plot_points(filename="captcha_points.txt"):
    points = []
    with open(filename, "r") as file:
        for line in file:
            x, y = map(float, line.split())
            points.append((x, y))
    
    x_vals = [p[0] for p in points]
    y_vals = [p[1] for p in points]
    
    plt.scatter(x_vals, y_vals, s=1)
    plt.title("MODELO CAPTCHA")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

# Generar y guardar puntos
iterations = 1000
points = generate_captcha_points(iterations)
save_points_to_file(points)

# Graficar los puntos
plot_points()
