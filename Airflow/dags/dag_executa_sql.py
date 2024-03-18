from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

with DAG(
        dag_id="dag_executa_sql", 
        start_date=datetime(2024, 3, 15),
        schedule="@daily",
        ) as dag:
    
    criar_tabela_db = PostgresOperator(
        task_id='criar_tabela_db',
        postgres_conn_id='postgres',
        sql="""
            CREATE TABLE IF NOT EXISTS TB_Teste(
                id        int,
                nome      VARCHAR(255)
            )
        """,
        dag=dag
    )
    
    insere_dados_tabela_db = PostgresOperator(
        task_id='insere_dados_tabela_db',
        postgres_conn_id='postgres',
        sql="""
            insert into TB_Teste( id, nome)
            values (10, 'Pamela')
        """,
        dag=dag
    )

criar_tabela_db >> insere_dados_tabela_db

