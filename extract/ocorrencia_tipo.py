import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from decouple import config

tipo_ocorrencia = pd.read_csv("Downloads/ocorrencia_tipo.csv", encoding='ISO-8859-1', delimiter=';')
tipo_ocorrencia = tipo_ocorrencia.rename(columns={'codigo_ocorrencia1': 'codigo_ocorrencia',
                                                  'ocorrencia_tipo': 'tipo_ocorrencia',
                                                  'ocorrencia_tipo_categoria': 'tipo_categoria_ocorrencia',
                                                  'taxonomia_tipo_icao': 'classificacao_tipo_ICAO'})
