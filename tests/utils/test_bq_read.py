from src.utils.bq_read import BQRead
from unittest.mock import patch
import pandas as pd
import pytest


def test_bq_read():
    mock_data = pd.DataFrame({
        'column1': [1, 2, 3],
        'column2': ['a', 'b', 'c']
    })
    config = {
        "bigquery": {
            "key_path": "./config/test_keys/service_account.json",
        }
    }
    with patch('src.utils.bq_read.BQRead.read_table', return_value=mock_data):
        bq_read = BQRead(config)  # Pass the config here
        df = bq_read.read_table("schema_rag.schema_rag")
        print(df.head())
        assert df.equals(mock_data)


def test_bq_read_error():
    config = {
        "bigquery": {
            "key_path": "./config/keys/service_account.json",
        }
    }
    bq_read = BQRead(config)
    with pytest.raises(Exception):
        bq_read.read_table("schema_rag.schema_rag")
