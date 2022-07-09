import shutil

import pandas as pd

Fuente = "C:/Users/con_acruzados/Documents/Reporte_Diario/prueba/resgistro_diario.xlsx"
Destino = "C:/Users/con_acruzados/Documents/Reporte_Diario/prueba/resgistro_diariod.xlsx"

shutil.copy(Fuente, Destino)
#shutil.copy("resgistro_diario.xlsx","C:/Users/con_acruzados/Documents/Reporte_Diario/prueba/resgistro_diariod.xlsx")
df = pd.read_excel("resgistro_diariod.xlsx", sheet_name='Hoja1')
df.describe()
print("Columns")
print(df.columns)

column = df.columns[1]
print(column)
print("-" * len(column))

for index, row in df.iterrows():
    print(row[column])
