from PyQt6 import QtCore
from PyQt6.QtWidgets import QPushButton, QFileDialog

from collection import collection_manager
from enums.enentNames import EventName
from utyllity import observer
from widgets.baseView import BaseView


class CollectionSettings(BaseView):
    def __init__(self, parent):
        super().__init__(parent)
        self.dialog_button = QPushButton(self)
        self.dialog_button.setText('Pick Main Collection')
        self.dialog_button.clicked.connect(self.show_dialog_butt)

    def show_dialog_butt(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        if dialog.exec() == QFileDialog.DialogCode.Accepted:
            collection_manager.set_collection_from_dir(dialog.selectedFiles()[0])
            observer.call_event(EventName.NEW_IMAGE)
        else:
            pass

