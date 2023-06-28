import math

# Parámetros del problema
n = 100  # número de átomos por lado
spacing = 1.0  # separación entre átomos
radius = 1.0  # radio de los átomos
charge_density = 0.0031255  # densidad de carga en e/Angstrom^2
e = 1.602176634e-19

# Calcula la carga de cada átomo
area = (n * spacing) ** 2
total_charge = area * charge_density
charge_per_atom = total_charge / (n ** 2)
    
# Genera las coordenadas de los átomos
coords = []
for i in range(-50,n-50):
    for j in range(-50,n-50):
        x = i * spacing
        y = -1.0
        z = j * spacing
        coords.append((x, y, z))

# Genera el archivo .pqr
with open("output-test.pqr", "w") as f:
    #f.write("ATOMS\n")
    for i, (x, y, z) in enumerate(coords):
        f.write(f"ATOM {i+1} H   H   1    {x:.3f} {y:.3f} {z:.3f}  {charge_per_atom:.3f}  {radius:.3f}\n")
    #f.write("END")

