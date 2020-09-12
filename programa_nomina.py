"""
Programa de Nomina de Empleados
"""

# creando diccionarios
empleado_1 = {'nombre': 'Lenin', 'edad': 35, 'telefono':'0992884077', 'salario': 1250.22, 'puesto':'Jefe'}
empleado_2 = {'nombre': 'Oscar', 'edad': 38, 'telefono':'0985543652', 'salario': 900.56, 'puesto':'Gerente'}
empleado_3 = {'nombre': 'Luis', 'edad': 28, 'telefono':'09965411226', 'salario': 700.22, 'puesto': 'Desarrollador'}
empleado_4 = {'nombre': 'Henry', 'edad': 35, 'telefono':'0992884077', 'salario': 800.25, 'puesto':'RRHH'}
empleado_5 = {'nombre': 'Ana', 'edad': 33, 'telefono':'0985543652', 'salario': 750.59, 'puesto':'Tecnico'}
empleado_6 = {'nombre': 'Maria', 'edad': 36, 'telefono':'09969811776', 'salario': 700.22, 'puesto': 'Desarrollador'}

lista_empleados = [empleado_1, empleado_2, empleado_3]
lista_desempleados=[empleado_4,empleado_5,empleado_6]

def imprimir_nomina(lista, nombre_nomina):

    print("\t\t\tNOMINA DE {}\n".format(nombre_nomina))
    print("**************************************************")
    print("NOMBRE", "EDAD", "SALARIO", "PUESTO", sep="\t\t")
    print("**************************************************")

    for empleado in lista:
        nombre_empleado = empleado['nombre']
        edad_empleado = empleado['edad']
        salario_empleado = empleado['salario']
        puesto_empleado = empleado['puesto']
        print(nombre_empleado, edad_empleado, salario_empleado, puesto_empleado, sep="\t\t")




#IMPRIMIR NOMINA DE EMPLEADOS
imprimir_nomina(lista=lista_empleados, nombre_nomina="EMPLEADOS")
imprimir_nomina(lista=lista_desempleados, nombre_nomina="DESEMPLEADOS")
print("FIN PROGRAMA")