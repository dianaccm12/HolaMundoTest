"""
Programa de Nomina de Empleados
"""
 # creando diccionarios
empleado_1 = {'nombre': 'Lenin', 'edad': 35, 'telefono':'0992884077', 'salario': 1250.22, 'puesto':'Jefe'}
empleado_2 = {'nombre': 'Oscar', 'edad': 38, 'telefono':'0985543652', 'salario': 900.56, 'puesto':'Gerente'}
empleado_3 = {'nombre': 'Luis', 'edad': 28, 'telefono':'09965411226', 'salario': 700.22, 'puesto': 'Desarrollador'}

lista_empleados = [empleado_1, empleado_2, empleado_3]

for empleado in lista_empleados:
    nombre_empleado = empleado['nombre'] 
    salario_empleado = empleado['salario']
    print(nombre_empleado, salario_empleado)