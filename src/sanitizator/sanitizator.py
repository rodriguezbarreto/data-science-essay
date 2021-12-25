import pandas as pd
import os


def sanitizator(origin, destiny):
    tables = os.listdir(origin)
    for table in tables:
        new_table = pd.read_csv(f'{origin}/{table}', on_bad_lines='skip')
        df = pd.DataFrame(new_table)
        df.to_csv(f'{destiny}/new_{os.path.basename(table)}')
