from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

with DAG('dag_viol_contra_mulher_mg', start_date= datetime(2024,3,15),
    schedule_interval= "30 * * * *", catchup =False,
    template_searchpath= ['/opt/airflow/csv', '/opt/airflow/python','/opt/airflow/sql']) as dag:

    extracao_limpeza= BashOperator(
        task_id='extracao_limpeza',
        bash_command= 'extracao_limpeza.py',
        dag=dag
    )
    
    criar_tabela_db= PostgresOperator(
        task_id='criar_tabela_db',
        postgres_conn_id='postgres',
        sql= 'criar_tabela_db.sql',
        dag=dag
    )
    
    insere_dados_tabela_db= PostgresOperator(
        task_id='insere_dados_tabela_db',
        postgres_conn_id='postgres',
        sql= 'insere_dados_tabela_db.sql',
        dag=dag
    )

extracao_limpeza >> criar_tabela_db >> insere_dados_tabela_db 
