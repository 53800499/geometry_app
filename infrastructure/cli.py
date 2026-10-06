from domain.circle import Circle
from domain.rectangle import Rectangle
from domain.cube import Cube
from domain.cylinder import Cylinder
from use_cases.calculate_area import CalculateArea
from use_cases.calculate_perimeter import CalculatePerimeter
from use_cases.calculate_volume import CalculateVolume

def run_cli():
    print("=== Calculatrice de Géométrie ===")

    while True:
        print("\nChoisissez une option :")
        print("1. Aire d'un cercle")
        print("2. Périmètre d'un rectangle")
        print("3. Volume d'un cube")
        print("4. Volume d'un cylindre")
        print("5. Quitter")

        choice = input("→ Votre choix : ")

        if choice == "1":
            r = float(input("Entrez le rayon : "))
            result = CalculateArea().execute(Circle(r))
            print(f"Aire = {result:.2f}")

        elif choice == "2":
            w = float(input("Entrez la largeur : "))
            h = float(input("Entrez la hauteur : "))
            result = CalculatePerimeter().execute(Rectangle(w, h))
            print(f"Périmètre = {result:.2f}")

        elif choice == "3":
            s = float(input("Entrez la longueur du côté : "))
            result = CalculateVolume().execute(Cube(s))
            print(f"Volume = {result:.2f}")

        elif choice == "4":
            r = float(input("Entrez le rayon : "))
            h = float(input("Entrez la hauteur : "))
            result = CalculateVolume().execute(Cylinder(r, h))
            print(f"Volume = {result:.2f}")

        elif choice == "5":
            print("Au revoir 👋")
            break

        else:
            print("Option invalide, veuillez réessayer.")
