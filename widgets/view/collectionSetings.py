from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QFileDialog, QWidget, QLabel

from collection import collection_manager
from enums.enentNames import EventName
from utyllity import observer
from widgets.shered.baseView import BaseView


class CollectionSettings(BaseView):
    def __init__(self, parent):
        super().__init__(parent)

        self.widget = QWidget(self)
        self.label = QLabel(self.widget)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.dialog_button = QPushButton(self.widget)
        self.dialog_button.setText('Pick Main Collection')
        self.dialog_button.clicked.connect(self.show_dialog_butt)

    def show_dialog_butt(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        if dialog.exec() == QFileDialog.DialogCode.Accepted:
            path = dialog.selectedFiles()[0]
            collection_manager.set_collection_from_dir(path)
            observer.call_event(EventName.NEW_COLLECTION)
            observer.call_event(EventName.NEW_IMAGE)
            self.label.setText(path)
        else:
            pass

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.widget.resize(self.size().width(), 40)
        self.dialog_button.resize(200, 40)
        self.label.resize(self.widget.size().width() - 200, self.widget.size().height())
        self.label.move(200, 0)
