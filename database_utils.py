import pandas as pd

class DatabaseConnector:

    def upload_date_times_data_to_db(self, date_times_data, table_name):
        engine = self.init_db_engine()
        date_times_data.to_sql(table_name, engine, if_exists='replace', index=False)
