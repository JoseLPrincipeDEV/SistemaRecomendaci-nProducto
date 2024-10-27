from lecturaDatos import *
import matplotlib.pyplot as plt
import tkinter as tk
from pandastable import Table, TableModel

#ANALISIS DE VENTA
#VOLUMEN POR VENTA DEL MES

#Obtenemos el mes de la fecha
df_ventas["mes"] = pd.to_datetime(df_ventas["fecha"]).dt.month

#agregamos el mes a la tabla y sumamos los valores numericos    
df_ventas_mensual = df_ventas.groupby("mes")["monto_total"].sum().reset_index()

#Creamos la funcion para mostrar en grafico el Volumen de ventas
def VolumenVentaPorMes():
    plt.bar(df_ventas_mensual["mes"], df_ventas_mensual["monto_total"])
    plt.title("VOLUMEN DE VENTA POR MES")
    plt.xlabel("MES")
    plt.ylabel("MONTO TOTAL")
    plt.xticks(range(1, 11))
    plt.show()

#Volumen de venta por ciudad

#DataFrame con la udion de dos DataFrame
df_ventas_usuario = pd.merge(df_ventas,df_usuarios, on = "id_usuario", how = "outer")

#DataFrame filtrando ciudad y sumamos monto total
df_ventas_ciudad = df_ventas_usuario.groupby("ciudad")["monto_total"].sum().reset_index()

#Funcion Para Graficar  el Volumen de vendad por ciudad
def VolumenVentaCiudad():
    plt.bar(df_ventas_ciudad["ciudad"], df_ventas_ciudad["monto_total"])
    plt.title("VOLUMEN DE VENTA POR CIUDAD")
    plt.xlabel("CIUDAD")
    plt.ylabel("MONTO TOTAL")
    plt.show()


## Creamos la clase DataFrameTable  que hereda de tk.Frame
class DataFrameTable(tk.Frame):
    #Definimos el constructor
    def __init__(self, parent=None, df=pd.DataFrame()):
        #Llamos al constructor de la clase base tk.Frame
        super().__init__()
        #Guardamos una referencia al widget padre
        self.parent = parent
        #Creamos la tabla
        self.pack(fill=tk.BOTH, expand=True)
        self.table = Table(
            self, dataframe=df,
            showtoolbar=False,
            showstatusbar=True,
            editable=False)
        #Mostramos la tabla
        self.table.show()
        #root = tk.Tk()
        #table = DataFrameTable(root, df_ventas_ciudad)
        #root.mainloop()
     
