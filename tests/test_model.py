from pathlib import Path
import pandas as pd
def test_assets(): assert Path("excel/Laurus_Labs_3_Statement_Model.xlsx").exists()
def test_data():
    d=pd.read_csv("data/raw/historical_financials.csv")
    assert len(d)==3 and d.revenue.is_monotonic_increasing
