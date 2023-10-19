import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from decouple import config

fator_contribuinte = pd.read_csv("data/fator_contribuinte.csv", encoding='ISO-8859-1', delimiter=';')
fator_contribuinte = fator_contribuinte.rename(columns={'codigo_ocorrencia3': 'codigo_ocorrencia',
                                                        'fator_nome': 'nome_fator',
                                                        'fator_aspecto': 'aspecto_fator',
                                                        'fator_area': 'area_fator'})
