import os
import unittest
from pathlib import Path

from get_item_evaluation import get_item_evaluation


class TestGetItemValueWithCSV(unittest.TestCase):
    DATA_DIR = Path(os.environ.get("DATADIR"))
    TEST_CSV_PATH = DATA_DIR.joinpath("plants/テストの台地.csv")
    TEST_DATA = [
        ["アイテム名", "豊穣期", "荒廃期", "異常気象"],
        ["ドス怪力の種", "3", "2", "1"],
        ["忍耐の種亜種", "0", "0.5", "3"],
    ]
    
    def setUp(self):
        """前処理: テスト用のCSVファイルを作成"""
        with self.TEST_CSV_PATH.open(mode="w", encoding="utf-8") as f:
            f.writelines(",".join(row) + "\n" for row in self.TEST_DATA)

    def tearDown(self):
        """後処理: テスト用のCSVファイルを削除"""
        if self.TEST_CSV_PATH.exists():
            self.TEST_CSV_PATH.unlink()

    def test_get_item_evaluation_from_csv(self):
        """CSVファイルから正しく値を取得できることを確認"""
        assert get_item_evaluation("テストの台地", "豊穣期", "ドス怪力の種") == 3
        assert get_item_evaluation("テストの台地", "荒廃期", "忍耐の種亜種") == 0.5

    def test_get_item_evaluation_not_found_in_csv(self):
        """存在しないアイテムの場合に0を返すことを確認"""
        assert get_item_evaluation("テストの台地", "狂走エキスG", "異常気象") == 0


if __name__ == "__main__":
    unittest.main()
