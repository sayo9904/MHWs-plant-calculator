import os
from pathlib import Path

import pytest

from domain import get_item_evaluation

DATA_DIR = Path(os.environ.get("DATADIR") or "")
TEST_CSV_PATH = DATA_DIR.joinpath("plants/テストの台地.csv")
TEST_DATA = [
    ["アイテム名", "豊穣期", "荒廃期", "異常気象"],
    ["ドス怪力の種", "3", "2", "1"],
    ["忍耐の種亜種", "0", "0.5", "3"],
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


def test_get_right_evaluation_value(setup_and_teardown):
    """指定した条件で正しい値を取得できることを確認"""
    assert get_item_evaluation("テストの台地", "豊穣期", "ドス怪力の種") == "3"
    assert get_item_evaluation("テストの台地", "荒廃期", "忍耐の種亜種") == "0.5"


def test_not_found_keys(setup_and_teardown):
    """存在しないアイテムの場合に0を返すことを確認"""
    assert get_item_evaluation("テストの台地", "異常気象", "狂走エキスG") == "0"


def test_file_not_found(setup_and_teardown):
    """存在しないファイルを指定したときにFileNotFoundErrorを返すことを確認"""
    with pytest.raises(FileNotFoundError):
        get_item_evaluation("存在しないマップ", "豊穣期", "ドス怪力の種")
