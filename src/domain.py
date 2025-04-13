import json
import os
from logging import config, getLogger
from pathlib import Path

import pandas as pd

from infrastructure import load_csv

with open("logging_config.json", "r") as f:
    log_conf = json.load(f)
config.dictConfig(log_conf)
logger = getLogger(__name__)


def get_item_evaluation(map_name: str, season_name: str, item_name: str) -> str:
    """
    ### What is this?:
        マップ、季節、アイテム名を指定して、対応する評価値を返します。

    ### Args:
        map_name (str): マップ名
        season_name (str): 季節名
        item_name (str): アイテム名

    ### Returns:
        float: 評価値を返します。対応するレコードがデータベースにない場合、0を返します。

    ### Usage:
        evaluated_value = get_item_value("隔ての砂原", "豊穣期", "ハチミツ") # to be 3
    """

    logger.debug(
        "Searching for evaluation value."
        f"map='{map_name}', season='{season_name}', item='{item_name}'"
    )

    data_dir = Path(os.environ.get("DATADIR") or "")
    plant_csv_path = data_dir.joinpath(f"plants/{map_name}.csv")

    df = load_csv(plant_csv_path)

    try:
        taeget_value = df.at[item_name, season_name]
    except KeyError:
        logger.info(f"'{item_name}' or '{season_name}' not found in the CSV.")
        return "0"

    return taeget_value


def get_map_seasons(rest_map_name: str, rest_season_name: str, target_map_name) -> str:
    """
    ### What is this?:
        マップ、季節を指定して休憩したとき、特定のマップがどの季節になるかを返します

    ### Args:
        rest_map_name (str): 休憩を行うマップ名
        rest_season_name (str): 休憩で指定する季節
        target_map_name (_type_): 調べたいマップ名

    ### Returns:
        str: 調べたいマップの季節

    ### Usage:
        my_get_map_seasons = get_map_seasons("隔ての砂原", "豊穣期, "緋の森") # to be "荒廃期"
    """
    if rest_map_name == "竜都の跡形":
        logger.error(f"map name: '{rest_map_name}' is invalid.")
        raise ValueError(f"'{rest_map_name}' is invalid.")

    season = ""
    return season
