from funciones import *
from lecturaDatos import *

def mostrar_menu_principal():
    print()
    print("#####################")
    print("BIENVENIDO AL SISTEMA")
    print("#####################")
    print()
    print("SELECCIONE UNA OPCIÓN")
    print("A) ANÁLISIS DE VENTA")
    print("B) VER TABLAS")
    print("C) CERRAR SISTEMA")
    print()

def mostrar_menu_analisis():
    print()
    print("A) VOLUMEN DE VENTA POR MES")
    print("B) VOLUMEN DE VENTA POR CIUDAD")  
    print("C) CERRAR SISTEMA")
    print()

def mostrar_menu_tablas():
    print()
    print("A) TABLA PRODUCTOS")
    print("B) TABLA USUARIOS")  
    print("C) TABLA VENTAS")
    print("D) CERRAR SISTEMA")
    print()

def sistema():
    while True:
        mostrar_menu_principal()
        opcion_uno = input().upper()

        if opcion_uno == "A":
            mostrar_menu_analisis()
            opcion_dos = input().upper()

            if opcion_dos == "A":
                VolumenVentaPorMes()
            elif opcion_dos == "B":
                VolumenVentaCiudad()
            elif opcion_dos == "C":
                print("SISTEMA FINALIZADO")
                break
            else:
                print("OPCIÓN INCORRECTA")

        elif opcion_uno == "B":
            mostrar_menu_tablas()
            opcion_tres = input().upper()

            if opcion_tres == "A":
                root = tk.Tk()
                table = DataFrameTable(root, df_productos)
                root.mainloop()
            elif opcion_tres == "B":
                root = tk.Tk()
                table = DataFrameTable(root, df_usuarios)
                root.mainloop()
            elif opcion_tres == "C":
                root = tk.Tk()
                table = DataFrameTable(root, df_ventas)
                root.mainloop()
            elif opcion_tres == "D":
                print("SISTEMA FINALIZADO")
                break
            else:
                print("OPCIÓN INCORRECTA")

        elif opcion_uno == "C":
            print("SISTEMA FINALIZADO")
            break
        else:
            print("OPCIÓN INCORRECTA")

sistema()