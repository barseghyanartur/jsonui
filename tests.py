import json
import unittest

from jsonui import DictToJsonConverter, JsonDiff, JsonToDictConverter
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication

app = QApplication([])  # QApplication instance

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2023-2024 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "TestDictToJsonConverter",
    "TestJsonDiff",
)


class TestDictToJsonConverter(unittest.TestCase):
    def test_conversion(self):
        converter = DictToJsonConverter()

        input_dict = "{'hello': 'world', 'isTrue': False}"
        expected_output = json.dumps(eval(input_dict), indent=4)

        QTest.qWaitForWindowExposed(converter)
        QTest.keyClicks(converter.input_text_edit, input_dict)
        QTest.mouseClick(converter.convert_button, Qt.LeftButton)

        actual_output = converter.output_text_edit.toPlainText()
        self.assertEqual(actual_output, expected_output)


class TestJsonToDictConverter(unittest.TestCase):
    def test_conversion(self):
        converter = JsonToDictConverter()

        input_json = (
            '{"hi": "you", "isTrue": true, "isFalse": false, "isNone": null}'
        )
        expected_output = json.loads(input_json)

        QTest.qWaitForWindowExposed(converter)
        QTest.keyClicks(converter.input_text_edit, input_json)
        QTest.mouseClick(converter.convert_button, Qt.LeftButton)

        actual_output = converter.output_text_edit.toPlainText()
        self.assertEqual(eval(actual_output), expected_output)


class TestJsonDiff(unittest.TestCase):
    def test_diff_detection(self):
        diff_viewer = JsonDiff()

        json1 = '{"name": "Alice", "age": 30}'
        json2 = '{"name": "Alice", "age": 31}'

        QTest.qWaitForWindowExposed(diff_viewer)
        QTest.keyClicks(diff_viewer.left_editor, json1)
        QTest.keyClicks(diff_viewer.right_editor, json2)
        QTest.mouseClick(diff_viewer.compare_button, Qt.LeftButton)

        # TODO: Add more tests
