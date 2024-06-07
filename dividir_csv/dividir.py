import pandas as pd

# Leer el archivo CSV
# df = pd.read_csv('productos.csv')
df = pd.read_csv('productos.csv', dtype={'Columna14': str})


# Dividir el DataFrame en partes
partes = 5
longitud_parte = len(df) // partes
for i, parte in enumerate(range(0, len(df), longitud_parte), 1):
    df_parte = df.iloc[parte:parte+longitud_parte]
    df_parte.to_csv(f'parte_{i}.csv', index=False)
