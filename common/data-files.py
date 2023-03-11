import os
import datetime

import fastparquet
import pandas as pd

ROOT = '/notebooks/data'

class DataFiles:
    @staticmethod
    def read(path):
        read_root_path = f'{ROOT}/{path}/'
        latest_date = sorted([dctry for dctry in os.listdir(read_root_path) if dctry != '.ipynb_checkpoints'], reverse=True)[0]
        
        return pd.read_parquet(f'{read_root_path}/{latest_date}')

    def write(path, df):
        write_path = f'{ROOT}/{path}/{datetime.date.today().isoformat()}'

        if not os.path.exists(write_path):
            os.makedirs(write_path)  

        df.to_parquet(f'{write_path}/data.parquet', index=False)