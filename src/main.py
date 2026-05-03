import kagglehub
import pandas as pd
import os

# baixar dataset
path = kagglehub.dataset_download("uciml/glass")

# montar caminho do arquivo
file_path = os.path.join(path, "glass.csv")

# ler dados
df = pd.read_csv(file_path)

# mostrar primeiras linhas
print(df)