# La libreria csv nos permite trabajar con archivos separados por comas
import csv

# La libreria copy nos permite tener datos de un archivo y usarlos dentro de un programa
import copy

# Creamos un dictionary
my_vehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# Se crea un ciclo for para imprimir cada una de las key : value que hay dentro del dictionary
for key, value in my_vehicle.items():
    print("{} : {}".format(key,value))
    
# Creamos una lista
my_inventory_list = []

# se abre el archivo car_fleet.csv y se guarda dentro de la variable csvFile
with open('car_fleet.csv') as csv_file:
    # Se lee el archivo donde su limitador son las comas
    csv_reader = csv.reader(csv_file, delimiter=',')  
    # Se crea e inicializa la variable lineCount
    line_count = 0  
    # Se lee cada una de las lineas, filas o renglones del archivo csvReader
    for row in csv_reader:
        # Si el valor de las lineas es 0
        if line_count == 0:
            # Se imprime el nombre de la columna
            print(f'Column names are: {", ".join(row)}')
            # y se incrementa en 1 el valor de la variable lineCount
            line_count += 1  
        # Si el valor de las lineas no es 0, imprime en cada una de las claves la posicion que fue separada por comas anteriormente 
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            # Se copia el valor de las variables dentro del dictionary my_vehicle
            currentVehicle = copy.deepcopy(my_vehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            # Se agrega a la lista un vehicle
            my_inventory_list.append(currentVehicle)  
            line_count += 1  
    # Se imprime el total de lineas/renglones/filas
    print(f'Processed {line_count} lines.')
    
    # Se crea un for para imprimir cada vehicle de la lista
    for myCarProperties in my_inventory_list:
        # Se imprimen los datos de cada vehicle
        for key, value in myCarProperties.items():
            # Se imprime la key  : value
            print("{} : {}".format(key,value))
            # Se imprime un separador   
            print("-----")