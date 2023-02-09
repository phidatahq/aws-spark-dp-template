from datetime import datetime

from airflow import DAG
from airflow.decorators import task

from airflow.providers.apache.spark.operators.spark_sql import SparkSqlOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

DAG_ID = "spark_test"

with DAG(
    dag_id=DAG_ID,
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=["example", "spark"],
) as dag:

    test_spark_submit = SparkSubmitOperator(
        application="${SPARK_HOME}/examples/src/main/python/pi.py", task_id="test_spark_submit"
    )

    test_spark_sql = SparkSqlOperator(
        sql="SELECT COUNT(1) as cnt FROM temp_table", task_id="test_spark_sql"
    )
