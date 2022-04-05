import pandas as pd
from pandas.testing import assert_frame_equal

def drop_duplicate_rows(df: pd.DataFrame) -> pd.DataFrame:
  """ Drops duplicate rows from a DataFrame
  """
  return df.drop_duplicates()


def test_replace_incorrect_number_format():
  df1 = pd.DataFrame({'a': [1, 2, 1], 'b': [3, 4, 3]})
  df2 = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
  assert_frame_equal(drop_duplicate_rows(df1), df2)