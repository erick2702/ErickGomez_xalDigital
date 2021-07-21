#Importamos librerias a utilizar
import requests
import  json
import pandas

url = 'https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow'
archivo = requests.get(url)
datos = archivo.json()['items']
print("--------------------------------------")
print("Ejercicio 1")
print(archivo)
print("--------------------------------------")

def Ejer1 (datos1):
#Inicializando las Variables
    Respuesta = 0
    NoRespuesta = 0
    for i in datos1:
        if i['is_answered'] == True:
            Respuesta += 1
        else:
            NoRespuesta += 1
    OutputEjeRe1 = "Numero respuestas contestadas = " + str(Respuesta)
    OutputEjeNo1 = "Numero respuestas NO contestadas = " + str(NoRespuesta)
    print("--------------------------------------")
    print("Ejercicio 2")
    print(OutputEjeRe1)
    print(OutputEjeNo1)
    print("--------------------------------------")

def Ejer2 (datos2):
    Owner = []
    for i in datos2:
        Owner.append(i["owner"]['reputation'])
    df_ower = pandas.DataFrame(Owner, columns=["Owner"] )
    df_ower.idxmax()
    mayor = df_ower.agg({"max"})
    print("--------------------------------------")
    print("Ejercicio 3")
    print(str(mayor))
    print("--------------------------------------")

def Ejer3(datos3):
    Views = []
    for i in datos3:
        Views.append(i["view_count"])
    df_Views = pandas.DataFrame(Views,columns=["Views"])
    df_Views.idxmin()
    menor = df_Views.agg({"min"})
    print("--------------------------------------")
    print("Ejercicio 4")
    print(str(menor))
    print("--------------------------------------")

def Ejer4(datos4):
    Activity_date = []
    for i in datos4:
        Activity_date.append(i["last_activity_date"])
        df_date = pandas.DataFrame(Activity_date, columns=["Activity_date"])
        df_date.idxmin()
        menor = df_date.agg({"min"})
        print(menor)


if __name__ == '__main__':
    #Ejercicio1
    Ejer1(datos1=datos)
    Ejer2(datos2=datos)
    Ejer3(datos3=datos)
    Ejer4(datos4=datos)

