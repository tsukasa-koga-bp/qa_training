import pandas as pd


class ServiceLoadDataset:
    def run(self, csv_path: str) -> pd.DataFrame:
        df_customer_info = pd.read_csv(
            csv_path,
            sep="\t",
        )
        return df_customer_info
