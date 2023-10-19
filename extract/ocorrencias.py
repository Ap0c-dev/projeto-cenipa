import numpy as np
import pandas as pd

df = pd.read_csv("data/ocorrencia.csv", encoding='ISO-8859-1', delimiter=';')
df = df.drop(columns=['codigo_ocorrencia1','codigo_ocorrencia2','codigo_ocorrencia3','codigo_ocorrencia4'])