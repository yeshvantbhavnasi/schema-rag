from google.cloud.bigquery import Client


class BQRead:
    def __init__(self, config):
        self.config = config
        self.bq_client = Client.from_service_account_json(
            config['bigquery']['key_path']
        )

    def read_table(self, table_id):
        try:
            dataset = self.bq_client.dataset(self.config.bigquery.dataset_id)
            # read table
            table = dataset.table(table_id)
            return table.to_dataframe()
        except Exception as e:
            # Log the error or handle it as needed
            print(f"An error occurred while reading the table: {e}")
            # Optionally, re-raise the exception or return a default value
            raise

    def export_data_to_gcs(self, table_id):
        # todo: implement gcs export
        pass
