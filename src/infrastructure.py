import json
import os
from logging import config, getLogger
from pathlib import Path

import pandas as pd

with open("logging_config.json", "r") as f:
    log_conf = json.load(f)
config.dictConfig(log_conf)
logger = getLogger(__name__)


def load_csv(file_name: str) -> pd.DataFrame:
    """
    ### What is this?:
        Dataディレクトリ以下に配置されたcsvを読み込む関数

    ### Args:
        file_name (str): ファイル名 (拡張子必須)

    ### Returns:
        pandas.DataFrame: 二次元のテーブル形式で返す

    ### Exceptions
        FileNotFoundError: ファイルを開くことができない場合

    ### Usage:
        my_data = load_csv("my_data.csv")
    """
    data_dir = Path(os.environ.get("DATADIR") or "")
    csv_path = data_dir.joinpath(file_name)

    try:
        logger.debug(f"Loading CSV file: {csv_path}")
        df = pd.read_csv(csv_path, index_col=0, encoding="utf-8", dtype=str)
    except FileNotFoundError:
        logger.error(f"'{csv_path}' not found.")
        raise FileNotFoundError
    logger.debug(f"Opened file '{csv_path}'")
    logger.debug(f"return dataframe: \n{df}")

    return df
