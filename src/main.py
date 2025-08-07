from decouple import config
import pandas as pd

archivo = config("ARCHIVO")
df = pd.read_excel(archivo)

print("Archivo cargado correctamente")
print(df.head())