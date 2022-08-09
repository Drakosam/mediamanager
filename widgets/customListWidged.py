from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QScrollArea, QPushButton, QWidget, QVBoxLayout, QLabel, QHBoxLayout

from widgets.baseView import BaseView
from collection import collection_manager
from enums.enentNames import EventName
from utyllity import observer

class CustomListWidget(BaseView):
    def __init__(self, parent: BaseView = None):
        super().__init__(parent)
        self.area = QScrollArea(self)
        self.area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.area.setWidgetResizable(True)
        self.item_list = []

        wid = QWidget()
        self.area.setWidget(wid)
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        wid.setLayout(self.layout)

    def add_item(self, text):
        item = CustomListWidgetItem()
        item.set_text(text)
        self.layout.addWidget(item)

    def clear(self):
        for i in range(len(self.item_list)):
            self.layout.removeItem(self.item_list[i])
            self.item_list[i].deleteLater()
            self.item_list[i] = None
        self.item_list = []

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.area.resize(self.size())


class CustomListWidgetItem(BaseView):
    def __init__(self, parent: BaseView = None):
        super().__init__(parent)
        self.set_background('#800')
        self.setMinimumHeight(60)
        self.setMaximumHeight(60)
        self.butt = QPushButton(self)
        self.label = QLabel('')
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout = QHBoxLayout()
        self.butt.setLayout(layout)
        layout.addWidget(self.label)

        self.butt.clicked.connect(self._update_selected_item)
        self.text = ''

    def _update_selected_item(self):
        collection_manager.set_collection_by_name(self.text)
        observer.call_event(EventName.NEW_IMAGE)

    def set_text(self, text):
        self.text = text
        self.label.setText(text)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.butt.resize(self.size())
