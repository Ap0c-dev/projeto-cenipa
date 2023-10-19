import numpy as np
import pandas as pd

df_aeronave = pd.read_csv("data/aeronave.csv", encoding='ISO-8859-1', delimiter=';')

df_aeronave = df_aeronave.rename(columns={'codigo_ocorrencia2': 'codigo_ocorrencia',
                                          'aeronave_matricula': 'maticula_da_aeronave',
                                          'aeronave_tipo_veiculo': 'tipo_de_aeronave',
                                          'aeronave_fabricante': 'fabricante',
                                          'aeronave_modelo': 'modelo',
                                          'aeronave_tipo_icao': 'tipo_ICAO',
                                          'aeronave_motor_tipo': 'tipo_de_motor',
                                          'aeronave_operador_categoria': 'categoria_de_operacao',
                                          'aeronave_motor_quantidade': 'quantidade_de_motores',
                                          'aeronave_pmd': 'peso_max_de_decolagem',
                                          'aeronave_pais_fabricante': 'pais_fabricante',
                                          'aeronave_pais_registro': 'pais_de_registro',
                                          'aeronave_registro_categoria': 'registro_categoria',
                                          'aeronave_registro_segmento': 'registro_segmento',
                                          'aeronave_voo_origem': 'origem_do_voo',
                                          'aeronave_voo_destino': 'destino_do_voo',
                                          'aeronave_fase_operacao': 'fase_de_operacao',
                                          'aeronave_nivel_dano': 'nivel_de_dano',
                                          'aeronave_fatalidades_total': 'total_de_fatalidades'})
