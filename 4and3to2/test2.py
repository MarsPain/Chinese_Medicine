import pandas as pd

with open("11000.csv", 'r', encoding="utf-8") as f:
    f.decode('unicode_escape')
    pd.read_csv(f)