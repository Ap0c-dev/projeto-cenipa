import os
from sqlalchemy import create_engine
from extract.aeronaves import df_aeronave
from dotenv import load_dotenv

# Carregando variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações para conexão com o PostgreSQL
db_config = {
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'host': os.environ.get('DB_HOST'),
    'port': os.environ.get('DB_PORT', '5432'),
    'database': os.environ.get('DB_NAME')
}

# Use SQLAlchemy para criar um engine para a conexão com o PostgreSQL
engine = create_engine(f'postgresql+psycopg2://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["database"]}')

# Persistindo o DataFrame na tabela do PostgreSQL
df_aeronave.to_sql('nome_da_tabela', engine, if_exists='replace', index=False)
