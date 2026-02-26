# Se usa la libreria re para trabajar con expresiones regulares
import re

# Abrimos el archivo de texto (la r es para leer(read))
with open("preproinsulin_seq.txt", "r") as f:
    # Leemos todo el contenido del archivo
    raw_data = f.read()

# Eliminamos la palabra ORIGIN
clean_data = re.sub(r"\bORIGIN\b", "", raw_data, flags=re.IGNORECASE)

# Eliminar el terminador de registro //, usamos la funcion replace para reemplazar los // por nada ajajajaj
clean_data = clean_data.replace("//", "")

# Eliminar/reemplazar cualquier cosa que no sea una letra
clean_data = re.sub(r"[^A-Za-z]", "", clean_data)

# Convertimos todo a minusculas
clean_data = clean_data.lower()

# Abrimos nuevamente el archivo txt (la w es para escribir(write))
with open("preproinsulin_seq.txt", "w") as f:
    # Limpiamos el archivo
    f.write(clean_data)
    
# Calculamos la longitud de preproinsulina con la funcion len()
print("Longitud preproinsulina = ", len(clean_data))

# Si la secuencia no tiene 110 caracteres nos salimos del programa con la funcion exit()
if len(clean_data) != 110:
    print("Error, la secuencia no tiene 110 caracteres")
    exit()
    
# Extraemos los primeros 24 caracteres 
lsinsulin = clean_data[0:24]

# Extraemos del caracter 25 al caracter 54
binsulin = clean_data[24:54]

# Extraemos del caracter 54 al caracter 55 al 89
cinsulin = clean_data[54:89]

# Extraemos del caracter 89 al 110
ainsulin = clean_data[89:110]

# Creamos los diferentes archivos 
with open("lsinsulin-seq-clean.txt", "w") as f:
    f.write(lsinsulin)
    
with open("binsulin-seq-clean.txt", "w") as f:
    f.write(binsulin)

with open("cinsulin-seq-clean.txt", "w") as f:
    f.write(cinsulin)
    
with open("ainsulin-seq-clean.txt", "w") as f:
    f.write(ainsulin)

# Verificamos el tamano de los caracteres
print("lsinsulin = ", len(lsinsulin))
print("binsulin = ", len(binsulin))
print("cinsulin = ", len(cinsulin))
print("ainsulin = ", len(ainsulin))

insulin = binsulin + ainsulin
# Total de insulina
print("Insulina procesada = ", len(insulin))

# Secuencia de la insulina 
print("Secuencia de la insulina = ", insulin)