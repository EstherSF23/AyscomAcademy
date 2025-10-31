import pandas as pd

def load_sales():
    df = pd.read_csv("source/sales.csv").drop_duplicates()
    df.columns = df.columns.str.lower()
    df = df.apply(lambda x: x.str.lower() if x.dtype == "object" else x)
    df["total"] = df["quantity"] * df["price"]
    print(df)
    return df
