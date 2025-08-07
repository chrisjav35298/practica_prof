
import pandas as pd
from sqlalchemy import create_engine
from decouple import config

archivo = config("ARCHIVO") 
df = pd.read_excel(archivo)

USER = config("USER")
PASSWORD = config("PASSWORD")
HOST = config("HOST")
PORT = config("PORT", cast=int) 
DATABASE = config("DATABASE")

# Aca se crea la conexión con SQLAlchemy
engine = create_engine(f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

# Se guarda el DataFrame en la base (se va a reemplazar si ya existe)
df.to_sql("tabla_info_salud", con=engine, if_exists="replace", index=False)

print(" Datos guardados en la base.")