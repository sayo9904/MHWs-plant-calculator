import os
from pathlib import Path

import pytest

from domain import get_map_seasons

DATA_DIR = Path(os.environ.get("DATADIR") or "")
TEST_CSV_PATH = DATA_DIR.joinpath("seasons/テストの砂原.csv")
TEST_DATA = [
    ["指定した季節", "テストの砂原", "テストの森", "テスト谷"],
    ["豊穣期", "豊穣期", "荒廃期", "異常気象"],
    ["荒廃期", "荒廃期", "異常気象", "豊穣期"],
    ["異常気象", "異常気象", "豊穣期", "荒廃期"],
]


@pytest.fixture
def setup_and_teardown():
    """前処理: テスト用のCSVファイルを作成"""
    with TEST_CSV_PATH.open(mode="w", encoding="utf-8") as f:
        f.writelines(",".join(row) + "\n" for row in TEST_DATA)

    yield
    """後処理: テスト用のCSVファイルを削除"""
    if TEST_CSV_PATH.exists():
        TEST_CSV_PATH.unlink()


def test_get_right_seasons(setup_and_teardown):
    """指定した条件で正しい値を取得できることを確認"""
    assert get_map_seasons("テストの砂原", "豊穣期", "テストの砂原") == "豊穣期"
    assert get_map_seasons("テストの砂原", "荒廃期", "テストの森") == "異常気象"
    assert get_map_seasons("テストの砂原", "荒廃期", "テスト谷") == "豊穣期"


def test_invalimap_name(setup_and_teardown):
    """無効のマップ名を指定したときにValueErrorを返すことを確認"""
    with pytest.raises(ValueError):
        get_map_seasons("竜都の跡形", "豊穣期", "テストの砂原")
