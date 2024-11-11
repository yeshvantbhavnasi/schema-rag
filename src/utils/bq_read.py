from google.cloud import bigquery


class BQRead:
    def __init__(self, config):
        self.config = config
        

    def read_table(self, table_id):
        # read the table from the bigquery 


    def export_data_to_gcs(self, table_id):
        # export the data to the gcs bucket 
    