#Librerías de interfaz gráfica y unidad de registros con pint
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pint import UnitRegistry

#Colores utilizados, algunos no son necesarios
global colores
colores = ["#d6c5c5","#c18b8b","#ffffff","#74737a","#00045F","#293244","#404244"]

#Menú principal
menu = Tk()
menu.title("Newton Conversor de Unidades Físicas")
menu.geometry("900x380")
menu.configure(bg=colores[4])
menu.resizable(False, False)

#Funciones para ejecución de las conversiones y cálculos de unidades
def Abrir_Convertidor_de_Unidades():
    ventana_cu = Toplevel()
    ventana_cu.title("Convertidor de Unidades - Menú")
    ventana_cu.geometry('500x350')
    ventana_cu.resizable(False, False)
    ventana_cu.configure(bg=colores[4])

    def Abrir_Longitud():
        ventana_longitud = Toplevel()
        ventana_longitud.title("Convertidor de Unidades - Longitud")
        ventana_longitud.geometry("628x263")
        ventana_longitud.resizable(False, False)

        frame = Frame(ventana_longitud)
        frame.configure(bg='#00056F')
        frame.pack()

        def convertir():
            numero = entrada1.get()
            unidad1 = primera_unidad.get().lower()
            unidad2 = segunda_unidad.get().lower()
            pruebax = 0
            try:
                test = float(numero)
                pruebax = 1
            except:
                messagebox.showerror(title="ERROR", message="¡Número Inválido!")

            if pruebax == 1:
                numero = float(numero)
                unidad = UnitRegistry()

                if unidad1 == "Metro":
                    numero *= unidad.meter
                elif unidad1 == "Kilómetro":
                    numero *= unidad.Kilometer
                elif unidad1 == "Centímetro":
                    numero *= unidad.centimeter
                elif unidad1 == "Milímetro":
                    numero *= unidad.millimeter
                elif unidad1 == "Milla":
                    numero *= unidad.mile
                elif unidad1 == "Pie":
                    numero *= unidad.foot
                conversion = str(numero.to(unidad2)).split()
                conversion = round(float(conversion[0]),6)
                entrada2.config(state="normal")
                entrada2.delete(0, END)
                entrada2.insert(0,conversion)
                entrada2.config(state="readonly")

        Convertir_Unidades = Label(frame, text="Convertidor de Unidades - Longitud", font="Times 30", bg=colores[4], fg=colores[2])
        de_etiqueta = Label(frame, text="De:", bg=colores[4], font="Times 15", fg=colores[2])
        a_etiqueta = Label(frame, text="A:", bg=colores[4], font="Times 15", fg=colores[2])
        entrada1 = Entry(frame, bg="white", font="Times 15", width=25)
        entrada2 = Entry(frame, bg="white", font="Times 15",state='readonly', width=25)
        primera_unidad = ttk.Combobox(frame, values=["Metro","Kilómetro", "Centímetro", "Milímetro", "Milla", "Pie"], font="Times 15")
        primera_unidad.current(0)
        segunda_unidad = ttk.Combobox(frame, values=["Meter","Kilómetro", "Centímetro", "Milímetro", "Milla", "Pie"], font="Times 15")
        segunda_unidad.current(1)
        boton_convertir = Button(frame, text="Convertir", command=convertir, bg=colores[5], fg="white", font="Times 15", relief='sunken')

        Convertir_Unidades.grid(row=0,column=0,columnspan=2,padx=10,pady=20)
        de_etiqueta.grid(row=1,column=0)
        a_etiqueta.grid(row=1,column=1)
        entrada1.grid(row=2,column=0, padx=30,pady=(0,20))
        entrada2.grid(row=2,column=1, padx=30,pady=(0,20))
        primera_unidad.grid(row=3,column=0, pady=(10,0))
        segunda_unidad.grid(row=3,column=1, pady=(10,0))
        boton_convertir.grid(row=4, column=0, columnspan=2, sticky="news", pady=10, padx=10)

    def Abrir_Temperatura():
        ventana_temperatura = Toplevel()
        ventana_temperatura.title("Convertidor de Unidades - Temperatura")
        ventana_temperatura.geometry("628x263")
        ventana_temperatura.resizable(False, False)

        #Convirtiendo unidades de temperatura
        def c_a_k(value):
            return value + 273.15
        def c_a_f(value):
            return ((value*9)/5)+32
        def k_a_c(value):
            return value - 273.15
        def k_a_f(value):
            return (((value-273.15)*9)/5)+32
        def f_a_c(value):
            return ((value-32)*5)/9
        def f_a_k(value):
            return (((value-32)*5)/9)+273.15
        #Asignando las fórmulas adecuadas con operación

        def Convertir_Temperatura():
            numero = entrada1.get()
            pruebax=0
            try:
                test = float(numero)
                pruebax=1
            except:
                messagebox.showerror(title="ERROR", message="¡Número Inválido!")
            if pruebax==1:
                numero = float(numero)
                unidad1 = primera_unidad.get()
                unidad2 = segunda_unidad.get()
                if unidad1 == unidad2:
                    resultado = numero
                else:
                    if unidad1 == "Celsius":
                        if unidad2 == "Kelvin":
                            resultado=c_a_k(numero)
                        else:
                            resultado=c_a_f(numero)
                    elif unidad1 == "Kelvin":
                        if unidad2 == "Celsius":
                            resultado=k_a_c(numero)
                        else:
                            resultado=k_a_f(numero)
                    elif unidad1 == "Fahrenheit":
                        if unidad2 == "Celsius":
                            resultado=f_a_c(numero)
                        else:
                            resultado=f_a_k(numero)
                entrada2.config(state="normal")
                entrada2.delete(0,END)
                entrada2.insert(0,resultado)
                entrada2.config(state="readonly")
        marco_temperatura = Frame(ventana_temperatura,bg=colores[4])
        marco_temperatura.pack()

        Convertir_Unidades = Label(marco_temperatura, text="Convertir Unidades - Temperatura", font="Times 30", bg=colores[4], fg=colores[2])
        de_etiqueta = Label(marco_temperatura, text="De:", bg=colores[4], font="Times 15", fg=colores[2])
        a_etiqueta = Label(marco_temperatura, text="A:", bg=colores[4], font="Times 15", fg=colores[2])
        entrada1 = Entry(marco_temperatura, bg="white", font="Times 15", width=25)
        entrada2 = Entry(marco_temperatura, bg="white", font="Times 15",state='readonly', width=25)
        primera_unidad = ttk.Combobox(marco_temperatura, values=["Celsius","Kelvin", "Fahrenheit"], font="Times 15")
        primera_unidad.current(0)
        segunda_unidad = ttk.Combobox(marco_temperatura, values=["Celsius","Kelvin", "Fahrenheit"], font="Times 15")
        segunda_unidad.current(1)
        boton_convertir = Button(marco_temperatura, text="Convert", command=Convertir_Temperatura, bg=colores[5], fg="white", font="Times 15", relief='sunken')

        Convertir_Unidades.grid(row=0,column=0,columnspan=2,padx=10,pady=20)
        de_etiqueta.grid(row=1,column=0)
        a_etiqueta.grid(row=1,column=1)
        entrada1.grid(row=2,column=0, padx=30,pady=(0,20))
        entrada2.grid(row=2,column=1, padx=30,pady=(0,20))
        primera_unidad.grid(row=3,column=0, pady=(10,0))
        segunda_unidad.grid(row=3,column=1, pady=(10,0))
        boton_convertir.grid(row=4, column=0, columnspan=2, sticky="news", pady=10, padx=10)

    def Abrir_Tiempo():
        ventana_temperatura = Toplevel()
        ventana_temperatura.title("Unit Converter - Time")
        ventana_temperatura.geometry("628x263")
        ventana_temperatura.resizable(False, False)

        #segundo a minuto
        def s_a_min(value):
            return value/60
        def s_a_h(value):
            return value/3600
        def s_a_d(value):
            return value/86400
        def s_a_mil(value):
            return value*1000
        #minuto a segundo
        def min_a_s(value):
            return value*60
        def min_a_h(value):
            return value/60
        def min_a_d(value):
            return value*0.0006944444
        def min_a_mil(value):
            return value*60000
        #hora a segundo
        def h_a_s(value):
            return value*3600
        def h_a_min(value):
            return value*60
        def h_a_d(value):
            return value*0.0416666667
        def h_a_mil(value):
            return value*3600000
        #dia a segundo
        def d_a_s(value):
            return value*86400
        def d_a_min(value):
            return value*1440
        def d_a_h(value):
            return value*24
        def d_a_mil(value):
            return value*86400000
        #milisegundo a segundo
        def mil_a_s(value):
            return value*0.001
        def mil_a_min(value):
            return value*0.0000166667
        def mil_a_8(value):
            return value/3600000
        def mil_a_d(value):
            return value/86400000
        #Iniciando conversiones de tiempo

        def Convertir_Tiempo():
            numero = entrada1.get()
            pruebax=0
            try:
                test = float(numero)
                pruebax=1
            except:
                messagebox.showerror(title="ERROR", message="¡Número Inválido!")
            if pruebax==1:
                numero = float(numero)
                unidad1,unidad2 = primera_unidad.get(),segunda_unidad.get()
                if unidad1 == unidad2:
                    entrada2.config(state="normal")
                    entrada2.delete(0,END)
                    entrada2.insert(0,numero)
                    entrada2.config(state="readonly")
                else:
                    if unidad1 == "Segundo":
                        if unidad2 == "Minuto":
                            resultado = s_a_min(numero)
                        elif unidad2 == "Hora":
                            resultado = s_a_h(numero)
                        elif unidad2 == "Dia":
                            resultado = s_a_d(numero)
                        elif unidad2 == "Milisegundo":
                            resultado = s_a_mil(numero)
                    elif unidad1 == "Minuto":
                        if unidad2 == "Segundo":
                            resultado = min_a_s(numero)
                        elif unidad2 == "Hora":
                            resultado = min_a_h(numero)
                        elif unidad2 == "Dia":
                            resultado = min_a_d(numero)
                        elif unidad2 == "Milisegundo":
                            resultado = min_a_mil(numero)
                    elif unidad1 == "Hora":
                        if unidad2 == "Segundo":
                            resultado = h_a_s(numero)
                        elif unidad2 == "Minuto":
                            resultado = h_a_min(numero)
                        elif unidad2 == "Dia":
                            resultado = h_a_d(numero)
                        elif unidad2 == "Milisegundo":
                            resultado = h_a_mil(numero)
                    elif unidad1 == "Dia":
                        if unidad2 == "Segundo":
                            resultado = d_a_s(numero)
                        elif unidad2 == "Minuto":
                            resultado = d_a_min(numero)
                        elif unidad2 == "Hora":
                            resultado = d_a_h(numero)
                        elif unidad2 == "Milisegundo":
                            resultado = d_a_mil(numero)
                    elif unidad1 == "Milisegundo":
                        if unidad2 == "Segundo":
                            resultado = mil_a_s(numero)
                        elif unidad2 == "Minuto":
                            resultado = mil_a_min(numero)
                        elif unidad2 == "Hora":
                            resultado = mil_a_8(numero)
                        elif unidad2 == "Dia":
                            resultado = mil_a_d(numero)
                    entrada2.config(state="normal")
                    entrada2.delete(0,END)
                    entrada2.insert(0,resultado)
                    entrada2.config(state="readonly")
        marco_temperatura = Frame(ventana_temperatura,bg=colores[4])
        marco_temperatura.pack()

        Convertir_Unidades = Label(marco_temperatura, text="Convertir Unidades - Tiempo", font="Times 30", bg=colores[4], fg=colores[2])
        de_etiqueta = Label(marco_temperatura, text="De:", bg=colores[4], font="Times 15", fg=colores[2])
        a_etiqueta = Label(marco_temperatura, text="A:", bg=colores[4], font="Times 15", fg=colores[2])
        entrada1 = Entry(marco_temperatura, bg="white", font="Times 15", width=25)
        entrada2 = Entry(marco_temperatura, bg="white", font="Times 15",state='readonly', width=25)
        primera_unidad = ttk.Combobox(marco_temperatura, values=["Segundo","Minuto", "Hora", "Dia", "Milisegundo"], font="Times 15")
        primera_unidad.current(0)
        segunda_unidad = ttk.Combobox(marco_temperatura, values=["Segundo","Minuto", "Hora", "Dia", "Milisegundo"], font="Times 15")
        segunda_unidad.current(1)
        boton_convertir = Button(marco_temperatura, text="Convertir", command=Convertir_Tiempo, bg=colores[5], fg="white", font="Times 15", relief='sunken')

        Convertir_Unidades.grid(row=0,column=0,columnspan=2,padx=10,pady=20)
        de_etiqueta.grid(row=1,column=0)
        a_etiqueta.grid(row=1,column=1)
        entrada1.grid(row=2,column=0, padx=30,pady=(0,20))
        entrada2.grid(row=2,column=1, padx=30,pady=(0,20))
        primera_unidad.grid(row=3,column=0, pady=(10,0))
        segunda_unidad.grid(row=3,column=1, pady=(10,0))
        boton_convertir.grid(row=4, column=0, columnspan=2, sticky="news", pady=10, padx=10)

    def Abrir_Velocidad():
        ventana_velocidad = Toplevel()
        ventana_velocidad.title("Convertir Unidades - Velocidad")
        ventana_velocidad.geometry("628x263")
        ventana_velocidad.resizable(False, False)


        #conversion de metro y segundo a kilometro por hora
        def ms_a_kh(evaluar):
            evaluar*=3.6
            return evaluar
        def ms_a_mh(evaluar):
            evaluar*=2.2369362921
            return evaluar
        def ms_a_mm(evaluar):
            evaluar*=3600
            return evaluar
        def ms_a_km(evaluar):
            evaluar*=0.06
            return evaluar
        #kilometro por hora a metro y segundo
        def kh_a_ms(evaluar):
            evaluar/=3.6
            return evaluar
        def kh_a_mh(evaluar):
            evaluar*=0.6213711922
            return evaluar
        def kh_a_mm(evaluar):
            evaluar*=16.66666666
            return evaluar
        def kh_a_km(evaluar):
            evaluar*=0.016666666
            return evaluar
        #metro por hora a metro por segundo
        def mh_a_ms(evaluar):
            evaluar*=0.44704
            return evaluar
        def mh_a_kh(evaluar):
            evaluar*=1.609344
            return evaluar
        def mh_a_mm(evaluar):
            evaluar*=26.8224
            return evaluar
        def mh_a_km(evaluar):
            evaluar*=0.0268224
            return evaluar
        #metro por minuto a metro por segundo
        def mm_a_ms(evaluar):
            evaluar*=0.016666666
            return evaluar
        def mm_a_kh(evaluar):
            evaluar*=0.06
            return evaluar
        def mm_a_mh(evaluar):
            evaluar*=0.0372822715
            return evaluar
        def mm_a_km(evaluar):
            evaluar*=0.001
            return evaluar
        #Conversión de kilómetro a otra unidad
        def km_a_ms(evaluar):
            evaluar*=16.66666666
            return evaluar
        def km_a_kh(evaluar):
            evaluar*=60
            return evaluar
        def km_a_mh(evaluar):
            evaluar*=37.282271534
            return evaluar
        def km_a_mm(evaluar):
            evaluar*=1000
            return evaluar
        #Convertir unidades de tiempo y medida

        def Convertir_Unidades():
            valor1 = entrada1.get()
            pruebax= 0
            try:
                test = float(valor1)
                pruebax = 1
            except:
                messagebox.showerror(title="ERROR", message="¡Número Inválido!")
            if pruebax == 1:
                valor1 = float(valor1)
                unidad1 = primera_unidad.get()
                unidad2 = segunda_unidad.get()
                if unidad1 == unidad2:
                    entrada2.config(state="normal")
                    entrada2.delete(0,END)
                    entrada2.insert(0,valor1)
                    entrada2.config(state="readonly")
                else:
                    if str(unidad1) == "Metro/Segundo":
                        if str(unidad2) == "Kilometro/Hora":
                            resultado = ms_a_kh(valor1)
                        elif str(unidad2) == "Milla/Hora":
                            resultado = ms_a_mh(valor1)
                        elif str(unidad2) == "Metro/Minuto":
                            resultado = ms_a_mm(valor1)
                        elif str(unidad2) == "Kilometro/Minuto":
                            resultado = ms_a_km(valor1)
                    elif str(unidad1) == "Kilometro/Hora":
                        if str(unidad2) == "Metro/Segundo":
                            resultado = kh_a_ms(valor1)
                        elif str(unidad2) == "Milla/Hora":
                            resultado = kh_a_mh(valor1)
                        elif str(unidad2) == "Metro/Minuto":
                            resultado = kh_a_mm(valor1)
                        elif str(unidad2) == "Kilometro/Minuto":
                            resultado = kh_a_km(valor1)
                    elif str(unidad1) == "Milla/Hora":
                        if str(unidad2) == "Metro/Segundo":
                            resultado = mh_a_ms(valor1)
                        elif str(unidad2) == "Kilometro/Hora":
                            resultado = mh_a_kh(valor1)
                        elif str(unidad2) == "Metro/Minuto":
                            resultado = mh_a_mm(valor1)
                        elif str(unidad2) == "Kilometro/Minuto":
                            resultado = mh_a_km(valor1)
                    elif str(unidad1) == "Metro/Minuto":
                        if str(unidad2) == "Metro/Segundo":
                            resultado = mm_a_ms(valor1)
                        elif str(unidad2) == "Kilometro/Hora":
                            resultado = mm_a_kh(valor1)
                        elif str(unidad2) == "Milla/Hora":
                            resultado = mm_a_mh(valor1)
                        elif str(unidad2) == "Kilometro/Minuto":
                            resultado = mm_a_km(valor1)
                    elif str(unidad1) == "Kilometro/Minuto":
                        if str(unidad2) == "Metro/Segundo":
                            resultado = km_a_ms(valor1)
                        elif str(unidad2) == "Kilometro/Hora":
                            resultado = km_a_kh(valor1)
                        elif str(unidad2) == "Milla/Hora":
                            resultado = km_a_mh(valor1)
                        elif str(unidad2) == "Metro/Minuto":
                            resultado = km_a_mm(valor1)
                    entrada2.config(state="normal")
                    entrada2.delete(0,END)
                    entrada2.insert(0,resultado)
                    entrada2.config(state="readonly")
                

        marco_velocidad = Frame(ventana_velocidad,bg=colores[4])
        marco_velocidad.pack()

        Convertir_Unidades = Label(marco_velocidad, text="Convertir Unidades - Velocidad", font="Times 30", bg=colores[4], fg=colores[2])
        de_etiqueta = Label(marco_velocidad, text="From:", bg=colores[4], font="Times 15", fg=colores[2])
        a_etiqueta = Label(marco_velocidad, text="To:", bg=colores[4], font="Times 15", fg=colores[2])
        entrada1 = Entry(marco_velocidad, bg="white", font="Times 15", width=25)
        entrada2 = Entry(marco_velocidad, bg="white", font="Times 15",state='readonly', width=25)
        primera_unidad = ttk.Combobox(marco_velocidad, values=["Metro/Segundo","Kilometro/Hora", "Milla/Hora", "Metro/Minuto", "Kilometro/Minuto"], font="Times 15")
        primera_unidad.current(0)
        segunda_unidad = ttk.Combobox(marco_velocidad, values=["Metro/Segundo","Kilometro/Hora", "Milla/Hora", "Metro/Minuto", "Kilometro/Minuto"], font="Times 15")
        segunda_unidad.current(1)
        boton_convertir = Button(marco_velocidad, text="Convert", command=Convertir_Unidades, bg=colores[5], fg="white", font="Times 15", relief='sunken')

        Convertir_Unidades.grid(row=0,column=0,columnspan=2,padx=10,pady=20)
        de_etiqueta.grid(row=1,column=0)
        a_etiqueta.grid(row=1,column=1)
        entrada1.grid(row=2,column=0, padx=30,pady=(0,20))
        entrada2.grid(row=2,column=1, padx=30,pady=(0,20))
        primera_unidad.grid(row=3,column=0, pady=(10,0))
        segunda_unidad.grid(row=3,column=1, pady=(10,0))
        boton_convertir.grid(row=4, column=0, columnspan=2, sticky="news", pady=10, padx=10)
    #Funciones principales terminadas

    marco_uc = Frame(ventana_cu, bg=colores[4])
    marco_uc.pack()

    titulo_newton = Label(marco_uc,text="Convertir Unidades - Menú", font="Times 30", bg=colores[4], fg=colores[2])
    subtitulo_newton = Label(marco_uc,text="Seleccionar un Tipo de Conversión", bg=colores[4], font="Times 20", fg=colores[2])

    boton_longitud = Button(marco_uc, text="Conversión de Longitud",command=Abrir_Longitud, bg=colores[5], font="Times 15", fg="white", relief='sunken')
    boton_temperatura = Button(marco_uc, text="Conversión de Temperatura",command=Abrir_Temperatura, bg=colores[5], font="Times 15", fg="white", relief='sunken')
    boton_tiempo = Button(marco_uc, text="Conversión de Tiempo",command=Abrir_Tiempo, bg=colores[5], font="Times 15", fg="white", relief='sunken')
    boton_peso = Button(marco_uc, text="Conversión de Velocidad",command=Abrir_Velocidad, bg=colores[5], font="Times 15", fg="white", relief='sunken')

    titulo_newton.grid(row=0, column=0,pady=(15,0))
    subtitulo_newton.grid(row=1, column=0,pady=10)

    boton_longitud.grid(row=2,column=0,sticky=NSEW,pady=5)
    boton_temperatura.grid(row=3,column=0,sticky=NSEW,pady=5)
    boton_tiempo.grid(row=4,column=0,sticky=NSEW,pady=5)
    boton_peso.grid(row=5,column=0,sticky=NSEW,pady=5)

def Salir():
    menu.destroy()    

def Abrir_FisicaBasica():
    ventana_cu = Toplevel()
    ventana_cu.title("Física Básica - Menú")
    ventana_cu.geometry('500x350')
    ventana_cu.resizable(False, False)
    ventana_cu.configure(bg=colores[4])
    #Iniciando las funciones con sus operaciones de unidades físicas

    def Abrir_Velocidad():
        ventana_fuerza = Toplevel()
        ventana_fuerza.title("Física Básica - Calculador de Velocidad")
        ventana_fuerza.configure(bg=colores[4])
        ventana_fuerza.geometry("580x300")
        ventana_fuerza.resizable(False, False)

        def CalcularFuerza():
            valor1=entrada_distancia.get()
            valor2=entrada_tiempo.get()
            valor3=entrada_velocidad.get()
            prueba_lista = [valor1,valor2,valor3]
            convertir_lista = []
            contador=0
            for cada in prueba_lista:
                if cada == "":
                    contador += 1
                else:
                    convertir_lista.append(cada)
            if contador != 1:
                messagebox.showerror(title="ERROR", message="¡Sólo debe haber una variable vacía para determinar!")
            else:
                try:
                    test=float(convertir_lista[0])+float(convertir_lista[1])
                except:
                    messagebox.showerror(title="ERROR", message="¡Número Inválido!") 
                    return
                if valor2!='' and valor3!='':
                    valor2,valor3 = float(valor2),float(valor3)
                    resultado = valor2*valor3
                    entrada_distancia.insert(0, resultado)
                elif valor2!="" and valor1!="":
                    valor2,valor1 = float(valor2),float(valor1)
                    resultado = valor1/valor2
                    entrada_velocidad.insert(0, resultado)
                else:
                    valor3,valor1 = float(valor3),float(valor1)
                    resultado = valor1/valor3
                    entrada_tiempo.insert(0, resultado)

        def Limpiar():
            entrada_distancia.delete(0,END)
            entrada_tiempo.delete(0,END)
            entrada_velocidad.delete(0,END)

        marco = Frame(ventana_fuerza)
        marco.configure(bg=colores[4])
        marco.pack()

        titulo_newton=Label(marco, text="Física Básica - Calculador de Velocidad",font="Times 30", bg=colores[4], fg=colores[2])
        etiqueta_distancia = Label(marco, text="Distancia (m)",font="Times 15", fg=colores[2],bg=colores[4])
        entrada_distancia = Entry(marco,font="Times 15")
        time_label = Label(marco, text="Tiempo (s)",font="Times 15", fg=colores[2],bg=colores[4])
        entrada_tiempo = Entry(marco,font="Times 15")
        velocity_label = Label(marco, text="Velocidad (m/s)",font="Times 15", fg=colores[2],bg=colores[4])
        entrada_velocidad = Entry(marco,font="Times 15")
        boton_Calcular = Button(marco,bg=colores[5],text="Calcular",font="Times 15", fg='white',relief="sunken",command=CalcularFuerza)
        button_Limpiar = Button(marco,bg=colores[5],text="Limpiar",font="Times 15", fg='white',relief="sunken",width=10,command=Limpiar)

        titulo_newton.grid(row=0,column=0,columnspan=2,pady=10)
        etiqueta_distancia.grid(row=1,column=0,sticky=E,pady=3)
        entrada_distancia.grid(row=1,column=1,sticky=W,pady=3)
        time_label.grid(row=2,column=0,sticky=E,pady=3)
        entrada_tiempo.grid(row=2,column=1,sticky=W,pady=3)
        velocity_label.grid(row=3,column=0,sticky=E,pady=3)
        entrada_velocidad.grid(row=3,column=1,sticky=W,pady=3)
        boton_Calcular.grid(row=4,column=0,columnspan=2,sticky=EW,pady=10)
        button_Limpiar.grid(row=5,column=0,columnspan=2,pady=10)
        
    def Abrir_Fuerza():
        ventana_fuerza = Toplevel()
        ventana_fuerza.title("Física Básica - Calculador de Fuerza")
        ventana_fuerza.configure(bg=colores[4])
        ventana_fuerza.geometry("580x300")
        ventana_fuerza.resizable(False, False)

        def CalcularFuerza():
            valor1=entrada_fuerza.get()
            valor2=entrada_masa.get()
            valor3=entrada_aceleracion.get()
            prueba_lista = [valor1,valor2,valor3]
            convertir_lista = []
            contador=0
            for cada in prueba_lista:
                if cada == "":
                    contador += 1
                else:
                    convertir_lista.append(cada)
            if contador != 1:
                messagebox.showerror(title="ERROR", message="¡Sólo debe haber una variable vacía para determinar!")
            else:
                try:
                    test=float(convertir_lista[0])+float(convertir_lista[1])
                except:
                    messagebox.showerror(title="ERROR", message="¡Número Inválido!") 
                    return
                if valor2!='' and valor3!='':
                    valor2,valor3 = float(valor2),float(valor3)
                    resultado = valor2*valor3
                    entrada_fuerza.insert(0, resultado)
                elif valor2!="" and valor1!="":
                    valor2,valor1 = float(valor2),float(valor1)
                    resultado = valor1/valor2
                    entrada_aceleracion.insert(0, resultado)
                else:
                    valor3,valor1 = float(valor3),float(valor1)
                    resultado = valor1/valor3
                    entrada_masa.insert(0, resultado)

        def Limpiar():
            entrada_fuerza.delete(0,END)
            entrada_aceleracion.delete(0,END)
            entrada_masa.delete(0,END)
        marco = Frame(ventana_fuerza)
        marco.configure(bg=colores[4])
        marco.pack()

        titulo_newton=Label(marco, text="Física Básica - Calculador de Fuerza",font="Times 30", bg=colores[4], fg=colores[2])
        etiqueta_fuerza = Label(marco, text="Fuerza (N)",font="Times 15", fg=colores[2],bg=colores[4])
        entrada_fuerza = Entry(marco,font="Times 15")
        masa_etiqueta = Label(marco, text="Masa (Kg)",font="Times 15", fg=colores[2],bg=colores[4])
        entrada_masa = Entry(marco,font="Times 15")
        etiqueta_aceleracion = Label(marco, text="Aceleración (m/s**2)",font="Times 15", fg=colores[2],bg=colores[4])
        entrada_aceleracion = Entry(marco,font="Times 15")
        boton_Calcular = Button(marco,bg=colores[5],text="Calcular",font="Times 15", fg='white',relief="sunken",command=CalcularFuerza)
        button_Limpiar = Button(marco,bg=colores[5],text="Limpiar",font="Times 15", fg='white',relief="sunken",width=10,command=Limpiar)

        titulo_newton.grid(row=0,column=0,columnspan=2,pady=10)
        etiqueta_fuerza.grid(row=1,column=0,sticky=E,pady=3)
        entrada_fuerza.grid(row=1,column=1,sticky=W,pady=3)
        masa_etiqueta.grid(row=2,column=0,sticky=E,pady=3)
        entrada_masa.grid(row=2,column=1,sticky=W,pady=3)
        etiqueta_aceleracion.grid(row=3,column=0,sticky=E,pady=3)
        entrada_aceleracion.grid(row=3,column=1,sticky=W,pady=3)
        boton_Calcular.grid(row=4,column=0,columnspan=2,sticky=EW,pady=10)
        button_Limpiar.grid(row=5,column=0,columnspan=2,pady=10)

    def Abrir_Aceleracion():
        ventana_fuerza = Toplevel()
        ventana_fuerza.title("Física Básica - Calculador de Aceleración")
        ventana_fuerza.configure(bg=colores[4])
        ventana_fuerza.geometry("650x320")
        #ventana_fuerza.resizable(False, False)
        
        def CalcularFuerza():
            valor1=entrada_velocidad_inicial.get()
            valor2=entrada_velocidad_final.get()
            valor3=entrada_tiempo.get()
            valor4=entrada_aceleracion.get()
            prueba_lista = [valor1,valor2,valor3,valor4]
            convertir_lista = []
            contador=0
            for cada in prueba_lista:
                if cada == "":
                    contador += 1
                else:
                    convertir_lista.append(cada)
            if contador != 1:
                messagebox.showerror(title="ERROR", message="¡Sólo debe haber una variable vacía para determinar!")
            else:
                try:
                    prueba1,prueba2,prueba3=float(convertir_lista[0]),float(convertir_lista[1]),float(convertir_lista[2])
                except:
                    messagebox.showerror(title="ERROR", message="¡Número Inválido!") 
                    return
                if valor1!='' and valor2!='' and valor3!='':
                    valor_final = (prueba2-prueba1)/prueba3
                    entrada_aceleracion.insert(0,valor_final)
                elif valor1!="" and valor3!="" and valor4!="":
                    valor_final = prueba1+(prueba3*prueba2)
                    entrada_velocidad_final.insert(0,valor_final)
                elif valor1!="" and valor2!="" and valor4!="":
                    valor_final = (prueba2-prueba1)/prueba3
                    if float(valor_final) < 0:
                        valor_final = str(valor_final) + " (Tiempo Negativo)"
                    entrada_tiempo.insert(0,valor_final)
                elif valor2!="" and valor3!="" and valor4!="":
                    valor_final = (prueba2*prueba3)-prueba1
                    valor_final = "-" + str(valor_final)
                    entrada_velocidad_inicial.insert(0,valor_final)
                print(valor_final)
        def Limpiar():
            entrada_velocidad_inicial.delete(0,END)
            entrada_velocidad_final.delete(0,END)
            entrada_tiempo.delete(0,END)
            entrada_aceleracion.delete(0,END)
        marco = Frame(ventana_fuerza)
        marco.configure(bg=colores[4])
        marco.pack()

        titulo_newton=Label(marco, text="Física Básica - Calculador de Aceleración",font="Times 30", bg=colores[4], fg=colores[2])
        etiqueta_velocidad_inicial = Label(marco, text="Velocidad Inicial (m/s)",font="Times 15", fg=colores[2],bg=colores[4])
        entrada_velocidad_inicial = Entry(marco,font="Times 15")
        etiqueta_velocidad_final = Label(marco, text="Velocidad Final (m/s)",font="Times 15", fg=colores[2],bg=colores[4])
        entrada_velocidad_final = Entry(marco,font="Times 15")
        time_label = Label(marco, text="Tiempo (s)",font="Times 15", fg=colores[2],bg=colores[4])
        entrada_tiempo = Entry(marco,font="Times 15")
        etiqueta_aceleracion = Label(marco, text="Aceleración (m/s**2)",font="Times 15", fg=colores[2],bg=colores[4])
        entrada_aceleracion = Entry(marco,font="Times 15")
        boton_Calcular = Button(marco,bg=colores[5],text="Calcular",font="Times 15", fg='white',relief="sunken",command=CalcularFuerza)
        button_Limpiar = Button(marco,bg=colores[5],text="Limpiar",font="Times 15", fg='white',relief="sunken",width=10,command=Limpiar)

        titulo_newton.grid(row=0,column=0,columnspan=2,pady=10)
        etiqueta_velocidad_inicial.grid(row=1,column=0,sticky=E,pady=3)
        entrada_velocidad_inicial.grid(row=1,column=1,sticky=W,pady=3)
        etiqueta_velocidad_final.grid(row=2,column=0,sticky=E,pady=3)
        entrada_velocidad_final.grid(row=2,column=1,sticky=W,pady=3)
        time_label.grid(row=3,column=0,sticky=E,pady=3)
        entrada_tiempo.grid(row=3,column=1,sticky=W,pady=3)
        etiqueta_aceleracion.grid(row=4,column=0,sticky=E,pady=3)
        entrada_aceleracion.grid(row=4,column=1,sticky=W,pady=3)
        boton_Calcular.grid(row=5,column=0,columnspan=2,sticky=EW,pady=10)
        button_Limpiar.grid(row=6,column=0,columnspan=2,pady=10)

    def Peso_Planeta():
        ventana_fuerza = Toplevel()
        ventana_fuerza.title("Física Básica - Peso en Planetas")
        ventana_fuerza.configure(bg=colores[4])
        ventana_fuerza.geometry("580x430")
        ventana_fuerza.resizable(False, False)

        def Calcular():
            pruebax=0
            try:
                test = float(entrada_peso.get())
                pruebax=1
            except:
                messagebox.showerror(title="ERROR", message="¡Número Inválido!")
            if pruebax==1:
                valor = entrada_peso.get()
                valor = float(valor)

                valor_luna=valor*0.167
                valor_mercurio=valor*0.4
                valor_venus=valor*0.9
                valor_marte=valor*0.4
                valor_jupiter=valor*2.3
                valor_saturno=valor*1.1
                valor_neptuno=valor*1.2
                valor_urano=valor*0.9
                valor_pluton=valor*0.1

                entrada_luna.config(state="normal")
                entrada_luna.delete(0,END)
                entrada_mercurio.config(state="normal")
                entrada_mercurio.delete(0,END)
                entrada_venus.config(state="normal")
                entrada_venus.delete(0,END)
                entrada_marte.config(state="normal")
                entrada_marte.delete(0,END)
                entrada_jupiter.config(state="normal")
                entrada_jupiter.delete(0,END)
                entrada_saturno.config(state="normal")
                entrada_saturno.delete(0,END)
                entrada_neptuno.config(state="normal")
                entrada_neptuno.delete(0,END)
                entrada_urano.config(state="normal")
                entrada_urano.delete(0,END)
                entrada_pluton.config(state="normal")
                entrada_pluton.delete(0,END)
                entrada_luna.insert(0,valor_luna)
                entrada_mercurio.insert(0,valor_mercurio)
                entrada_venus.insert(0,valor_venus)
                entrada_marte.insert(0,valor_marte)
                entrada_jupiter.insert(0,valor_jupiter)
                entrada_saturno.insert(0,valor_saturno)
                entrada_neptuno.insert(0,valor_neptuno)
                entrada_urano.insert(0,valor_urano)
                entrada_pluton.insert(0,valor_pluton)
                entrada_luna.config(state="readonly")
                entrada_mercurio.config(state="readonly")
                entrada_venus.config(state="readonly")
                entrada_marte.config(state="readonly")
                entrada_jupiter.config(state="readonly")
                entrada_saturno.config(state="readonly")
                entrada_neptuno.config(state="readonly")
                entrada_urano.config(state="readonly")
                entrada_pluton.config(state="readonly")

        marco = Frame(ventana_fuerza)
        marco.configure(bg=colores[4])
        marco.pack()

        titulo_newton=Label(marco, text="Física Básica - Peso en Planetas",font="Times 30", bg=colores[4], fg=colores[2])
        etiqueta_peso = Label(marco, text="Su Peso (Kg)",font="Times 15", fg=colores[2],bg=colores[4])
        entrada_peso = Entry(marco,font="Times 15")
        boton = Button(marco, font="Times 15",text="Calcular",command=Calcular, bg=colores[5], fg="white")
        etiqueta_luna = Label(marco, font="Times 15",text="Luna: ",bg=colores[4])
        entrada_luna = Entry(marco, font="Times 15",state="readonly")
        etiqueta_mercurio = Label(marco, font="Times 15",text="Mercurio: ",bg=colores[4])
        entrada_mercurio = Entry(marco, font="Times 15",state="readonly")
        venus_label = Label(marco, font="Times 15",text="Venus: ",bg=colores[4])
        entrada_venus = Entry(marco, font="Times 15",state="readonly")
        etiqueta_marte = Label(marco, font="Times 15",text="Marte: ",bg=colores[4])
        entrada_marte = Entry(marco, font="Times 15",state="readonly")
        etiqueta_jupiter = Label(marco, font="Times 15",text="Jupiter: ",bg=colores[4])
        entrada_jupiter = Entry(marco, font="Times 15",state="readonly")
        etiqueta_saturno = Label(marco, font="Times 15",text="Saturno: ",bg=colores[4])
        entrada_saturno = Entry(marco, font="Times 15",state="readonly")
        etiqueta_neptuno = Label(marco, font="Times 15",text="Neptuno: ",bg=colores[4])
        entrada_neptuno = Entry(marco, font="Times 15",state="readonly")
        etiqueta_urano = Label(marco, font="Times 15",text="Urano: ",bg=colores[4])
        entrada_urano = Entry(marco, font="Times 15",state="readonly")
        etiqueta_pluton = Label(marco, font="Times 15",text="Pluton: ",bg=colores[4])
        entrada_pluton = Entry(marco, font="Times 15",state="readonly")

        titulo_newton.grid(row=0,column=0,columnspan=2,pady=10)
        etiqueta_peso.grid(row=1,column=0,sticky=E,pady=3)
        entrada_peso.grid(row=1,column=1,sticky=W,pady=3)
        boton.grid(row=2,column=0,columnspan=2,sticky=EW,pady=10)
        etiqueta_luna.grid(row=3,column=0, sticky="E")
        entrada_luna.grid(row=3,column=1, sticky="W")
        etiqueta_mercurio.grid(row=4,column=0, sticky="E")
        entrada_mercurio.grid(row=4,column=1, sticky="W")
        venus_label.grid(row=5,column=0, sticky="E")
        entrada_venus.grid(row=5,column=1, sticky="W")
        etiqueta_marte.grid(row=6,column=0, sticky="E") 
        entrada_marte.grid(row=6,column=1, sticky="W") 
        etiqueta_jupiter.grid(row=7,column=0, sticky="E")
        entrada_jupiter.grid(row=7,column=1, sticky="W")
        etiqueta_saturno.grid(row=8,column=0, sticky="E")
        entrada_saturno.grid(row=8,column=1, sticky="W")
        etiqueta_neptuno.grid(row=9,column=0, sticky="E")
        entrada_neptuno.grid(row=9,column=1, sticky="W")
        etiqueta_urano.grid(row=10,column=0, sticky="E")
        entrada_urano.grid(row=10,column=1, sticky="W")
        etiqueta_pluton.grid(row=11,column=0, sticky="E")
        entrada_pluton.grid(row=11,column=1, sticky="W")
    #Funciones finalizadas y a continuación la estructura

    marco_uc = Frame(ventana_cu, bg=colores[4])
    marco_uc.pack()

    titulo_newton = Label(marco_uc,text="Física Básica - Menú", font="Times 30", bg=colores[4], fg=colores[2])
    subtitulo_newton = Label(marco_uc,text="Seleccionar un tipo de Cáculo", bg=colores[4], font="Times 20", fg=colores[2])

    boton_longitud = Button(marco_uc, text="Calculador de Velocidad",command=Abrir_Velocidad, bg=colores[5], font="Times 15", fg="white", relief='sunken')
    boton_temperatura = Button(marco_uc, text="Calculador de Fuerza",command=Abrir_Fuerza, bg=colores[5], font="Times 15", fg="white", relief='sunken')
    boton_tiempo = Button(marco_uc, text="Calculador de Aceleración",command=Abrir_Aceleracion, bg=colores[5], font="Times 15", fg="white", relief='sunken')
    boton_peso = Button(marco_uc, text="Peso en Planetas",command=Peso_Planeta, bg=colores[5], font="Times 15", fg="white", relief='sunken')

    titulo_newton.grid(row=0, column=0,pady=(15,0))
    subtitulo_newton.grid(row=1, column=0,pady=10)

    boton_longitud.grid(row=2,column=0,sticky=NSEW,pady=5)
    boton_temperatura.grid(row=3,column=0,sticky=NSEW,pady=5)
    boton_tiempo.grid(row=4,column=0,sticky=NSEW,pady=5)
    boton_peso.grid(row=5,column=0,sticky=NSEW,pady=5)

#Marco o Frame que contiene las opciones de elección
marco = Frame(menu, bg=colores[4])
marco.pack()

titulo_newton = Label(marco,text="Newton Conversor de Unidades Físicas", font="Times 35", bg=colores[4], fg=colores[2])
subtitulo_newton = Label(marco,text="Seleccione una categoría", bg=colores[4], font="Times 25", fg=colores[2])
button1 = Button(marco, text="Convertir Unidades", bg=colores[5], font="Times 20", fg="white", relief='sunken', command=Abrir_Convertidor_de_Unidades)
button2 = Button(marco, text="Física Básica", bg=colores[5], font="Times 20", fg="white", relief='sunken', command=Abrir_FisicaBasica)
button3 = Button(marco, text="Salir de la Aplicación", bg=colores[5], font="Times 20", fg="white", relief='sunken', command=Salir)

titulo_newton.grid(row=0, column=0,pady=(15,0),padx=20)
subtitulo_newton.grid(row=1, column=0,pady=10)
button1.grid(row=2,column=0,sticky=NSEW,pady=5,padx=10)
button2.grid(row=3,column=0,sticky=NSEW,pady=5,padx=10)
button3.grid(row=4,column=0,sticky=NSEW,pady=5,padx=10)

menu.mainloop()