from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 18),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1
}

dag = DAG('simple_dag', default_args=default_args, schedule_interval='@daily')

start_task = DummyOperator(task_id='start', dag=dag)
task1 = BashOperator(task_id='task1', bash_command='echo "Hello from Task 1"', dag=dag)
task2 = BashOperator(task_id='task2', bash_command='echo "Hello from Task 2"', dag=dag)
end_task = DummyOperator(task_id='end', dag=dag)

start_task >> task1 >> task2 >> end_task
