from pathlib import Path
import pandas as pd
d=pd.read_csv("data/raw/historical_financials.csv")
assert d.revenue.is_monotonic_increasing
assert (d.pat>0).all()
assert Path("excel/Laurus_Labs_3_Statement_Model.xlsx").exists()
print("PASS: Laurus Labs 3-statement project validation")
