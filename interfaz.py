from funciones import *
from lecturaDatos import *

def sistema():
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

    opcion_uno = input().upper()

    if opcion_uno == "A":
        print()
        print("A) VOLUMEN DE VENTA POR MES")
        print("B) VOLUMEN DE VENTA POR CIUDAD")  
        print("C) CERRAR SISTEMA")

        opcion_dos = input().upper()

        if opcion_dos == "A" :
            VolumenVentaPorMes()
            sistema()
        elif opcion_dos == "B" :
            VolumenVentaCiudad()
            sistema()
        elif opcion_dos == "C":
            print("SISTEMA FINALIZADO" )
        else:
            print()
            print("OPCIÓN INCORRECTA")
            print()
            sistema()

        sistema()

    elif opcion_uno == "B":
        print()
        print("A) TABLA PRODUCTOS")
        print("B) TABLA USUARIOS")  
        print("C) TABLA VENTAS")
        print("D) CERRAR SISTEMA")
        
        opcion_tres = input().upper()

        if opcion_tres == "A" :
            root = tk.Tk()
            table = DataFrameTable(root, df_productos)
            root.mainloop()
        elif opcion_tres == "B" :
            root = tk.Tk()
            table = DataFrameTable(root, df_usuarios)
            root.mainloop()
        elif opcion_tres == "C" :
            root = tk.Tk()
            table = DataFrameTable(root, df_ventas)
            root.mainloop()
        elif opcion_tres == "D":
            print("SISTEMA FINALIZADO" )
            return "SISTEMA FINALIZADO"
        else:
            print()
            print("OPCIÓN INCORRECTA")
            print()
            sistema()

        sistema()

    elif opcion_uno == "C":

        print("SISTEMA FINALIZADO" )
        return "SISTEMA FINALIZADO" 
    
    else:
        print("OPCIÓN INCORRECTA" )
        sistema()
    
sistema()