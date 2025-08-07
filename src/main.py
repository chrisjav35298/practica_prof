from decouple import config
import pandas as pd

archivo = config("ARCHIVO")
df = pd.read_excel(archivo)  #se esta definiendo un dataframe, que va a pasar a llamarse df

print("Archivo cargado correctamente")
print(df.head())
print(df.info())