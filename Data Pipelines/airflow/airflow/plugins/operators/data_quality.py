from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class DataQualityOperator(BaseOperator):

    ui_color = "#89DA59"

    @apply_defaults
    def __init__(self, 
                 redshift_conn_id="", 
                 dq_checks=[], 
                 * args, 
                 **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)

        self.redshift_conn_id = redshift_conn_id
        self.dq_checks = dq_checks

    def execute(self, context):

        redshift_hook = PostgresHook(self.redshift_conn_id)

        for check in self.dq_checks:
            sql_query = check.get('check_sql')
            result_val = check.get('expected_result')
            number_of_observations = redshift_hook.get_records(sql_query)
            
            if number_of_observations[0][0] == result_val:
                raise ValueError(f"Data Quality check {sql_query} has failed")
            
            self.log.info(f"Data Quality check {sql_query} successful")
            

