
import pandas as pd
import csv
df = pd.DataFrame()

url_1="https://dados.mg.gov.br/dataset/ab7e00b6-a8ae-4426-8809-85e23f3f6b6f/resource/e4f313cf-28ed-4a89-9dcc-c8c0382f1fdf/download/violencia_domestica_2021.csv"
url_2="https://dados.mg.gov.br/dataset/ab7e00b6-a8ae-4426-8809-85e23f3f6b6f/resource/3075b898-19f0-4769-ab8e-2f56cabfd7ba/download/violencia_domestica_2022.csv"
url_3="https://dados.mg.gov.br/dataset/ab7e00b6-a8ae-4426-8809-85e23f3f6b6f/resource/f2957178-7f1d-4890-84af-a2aeb5e603fb/download/violencia_domestica_2023.csv"
dados_viol_mulher_23 = pd.read_csv(url_3,sep=';',encoding='utf-8')
dados_viol_mulher_22 = pd.read_csv(url_2,sep=';',encoding='utf-8')
dados_viol_mulher_21 = pd.read_csv(url_1,sep=';',encoding='utf-8')

dados_viol_mulher = pd.concat([dados_viol_mulher_23, dados_viol_mulher_22, dados_viol_mulher_21], ignore_index=True)

#Limpeza

remover=['municipio_cod','data_fato']
df_dados_viol_mulher= dados_viol_mulher.drop(remover, axis=1)



# Salvar o DataFrame em um diretório
diretorio = '/opt/airflow/csv/'
nome_do_arquivo = 'dados_viol_mulher.csv'
caminho_completo = diretorio + nome_do_arquivo

df.to_csv(caminho_completo, index=False) 