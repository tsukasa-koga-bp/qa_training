import pandas as pd
from pandas.testing import assert_frame_equal


class MyAssert:
    def assert_df(self, df_results: pd.DataFrame, df_expected: pd.DataFrame) -> None:
        assert_frame_equal(df_results, df_expected, check_dtype=False)
