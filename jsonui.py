import json
import sys

from deepdiff import DeepDiff
from PyQt5.Qsci import QsciLexerJSON, QsciScintilla
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QTabWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

__title__ = "jsonui"
__version__ = "0.1"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2023-2024 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "DictToJsonConverter",
    "JsonDiff",
    "MainApplication",
    "apply_highlight",
    "find_line_number_for_path",
    "highlight_differences",
    "main",
)

# **************************************************************************
# ****************************** JSON diff *********************************
# **************************************************************************


class JsonDiff(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        # Setup JSON editors
        self.left_editor = self.create_editor()
        self.right_editor = self.create_editor()

        self.compare_button = QPushButton("Compare JSONs")
        self.compare_button.clicked.connect(self.compare_jsons)

        # Layout
        layout.addWidget(self.left_editor)
        layout.addWidget(self.compare_button)
        layout.addWidget(self.right_editor)

        self.setLayout(layout)

    def create_editor(self):
        editor = QsciScintilla()
        lexer = QsciLexerJSON()
        editor.setLexer(lexer)
        editor.setAutoIndent(True)
        editor.setIndentationWidth(4)
        return editor

    def compare_jsons(self):
        left_text = self.left_editor.text()
        right_text = self.right_editor.text()

        try:
            left_json = json.loads(left_text)
            right_json = json.loads(right_text)
        except json.JSONDecodeError:
            print("Error decoding JSON")
            return

        diff = DeepDiff(left_json, right_json, ignore_order=False)
        if diff:
            highlight_differences(self.left_editor, diff)
            highlight_differences(
                self.left_editor, diff
            )  # TODO: Get rid of the 2nd one
            highlight_differences(self.right_editor, diff)
            highlight_differences(
                self.right_editor, diff
            )  # TODO: Get rid of the 2nd one
            # This is where you'd call a more sophisticated version of `highlight_differences`
            # For now, just indicating there are differences
            print("Differences detected.")
        else:
            print("No differences.")


def highlight_differences(editor, diff):
    # Simplified approach: Iterate through the changes and highlight
    for change_type, changes in diff.items():
        if change_type == "dictionary_item_added":
            # Handle new items (simplified example, assumes we can find the position)
            for added_path in changes:
                # Here, you'd need to find the line number for the added item
                line_num = find_line_number_for_path(editor, added_path)
                apply_highlight(
                    editor, line_num, QColor("#4ba2ff")
                )  # Example color for addition

        elif change_type == "values_changed":
            for path, change in changes.items():
                # Handle changed values
                line_num = find_line_number_for_path(editor, path)
                apply_highlight(
                    editor, line_num, QColor("#E5E833")
                )  # Example color for changes


def find_line_number_for_path(editor, path):
    """Find the line number for a given JSON path in a QScintilla editor.

    :param editor: QScintilla editor instance containing JSON text.
    :param path: String path in the format "root['key']['subkey']" or similar.
    :return: Line number (int) where the path points to in the editor, or -1 if not found.
    """
    # Convert the path string to a list of keys (assuming path is well-formed)
    keys = (
        path.strip("root")
        .replace("']['", ".")
        .strip("['")
        .rstrip("']")
        .split(".")
    )

    text_lines = editor.text().split("\n")
    current_nesting_level = 0
    line_number = -1

    for i, line in enumerate(text_lines):
        # Check for opening and closing braces to track nesting level
        current_nesting_level += line.count("{") - line.count("}")
        current_nesting_level += line.count("[") - line.count("]")

        # Prepare to match the line with the current key in the path
        current_key = keys[0] if keys else None
        if (
            current_key
            and f"'{current_key}'" in line
            or f'"{current_key}"' in line
        ):
            # Found the key, remove it from the path list and update line_number
            keys.pop(0)
            line_number = i

            if not keys:  # If no more keys, path fully matched
                break

            # Reset nesting level after matching a key (assuming keys are unique at each level)
            current_nesting_level = 0

    if keys:  # Not all keys were matched
        return -1

    return line_number


def apply_highlight(editor, line_num, color):
    """Apply highlight to a specific line in the QScintilla editor."""
    editor.markerDefine(QsciScintilla.Background, line_num)
    editor.setMarkerBackgroundColor(color, line_num)
    editor.markerAdd(line_num, 0)  # 0 is the marker number for simplicity


# **************************************************************************
# ************************* Dict to JSON converter *************************
# **************************************************************************


class DictToJsonConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Create the text edit widgets for input and output
        self.input_text_edit = QTextEdit()
        self.input_text_edit.setPlaceholderText("Enter Python dict here...")
        self.output_text_edit = QTextEdit()
        self.output_text_edit.setPlaceholderText(
            "Formatted JSON will appear here..."
        )
        self.output_text_edit.setReadOnly(True)  # Make output read-only

        # Create the convert button
        self.convert_button = QPushButton("Convert to JSON")
        self.convert_button.clicked.connect(self.convert_input)

        # Add widgets to the layout
        layout.addWidget(self.input_text_edit)
        layout.addWidget(self.convert_button)
        layout.addWidget(self.output_text_edit)

        # Set the layout on the application's window
        self.setLayout(layout)

    def convert_input(self):
        # Get the input text
        input_text = self.input_text_edit.toPlainText()
        try:
            # Convert the input string to a Python dict
            input_dict = eval(input_text)
            # Convert the dict to a JSON string
            json_str = json.dumps(input_dict, indent=4)
            # Display the JSON string in the output text edit
            self.output_text_edit.setText(json_str)
        except Exception as e:
            self.output_text_edit.setText(f"Error: {str(e)}")


# **************************************************************************
# ******************************* Main app *********************************
# **************************************************************************


class MainApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set up the layout
        self.layout = QVBoxLayout()
        self.tabs = QTabWidget()
        self.dict_to_json_tab = DictToJsonConverter()
        self.json_diff_tab = JsonDiff()

        self.tabs.addTab(self.dict_to_json_tab, "Dict to JSON Converter")
        self.tabs.addTab(self.json_diff_tab, "JSON Diff")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        self.setWindowTitle("Python JSON Tools")
        self.resize(1000, 800)  # Resize the window


def main():
    app = QApplication(sys.argv)
    main_window = MainApplication()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
