from PyQt5.Qt import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)

EMPTY_MESSAGE = "The input is empty.\n"


def update_readout(input_string, readout_widget):
    if input_string:
        message = f"‘{input_string}’\ncontains {len(input_string)} characters."
    else:
        message = EMPTY_MESSAGE
    readout_widget.setText(message)


def main():
    app = QApplication([])

    window = QWidget()
    window.show()

    vertical_layout = QVBoxLayout()
    window.setLayout(vertical_layout)
    window.resize(500, 100)

    label = QLabel("Enter an input string:")
    label.setAlignment(Qt.AlignCenter)

    text_field = QLineEdit("")
    readout = QLabel(EMPTY_MESSAGE)
    readout.setAlignment(Qt.AlignCenter)
    text_field.textChanged.connect(
        lambda input_string: update_readout(input_string, readout)
    )

    vertical_layout.addWidget(label)
    vertical_layout.addWidget(text_field)
    vertical_layout.addWidget(readout)
    app.exec_()


if __name__ == "__main__":
    main()
