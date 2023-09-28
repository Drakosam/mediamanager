from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QPushButton

from collection import collection_manager
from enums.enentNames import EventName
from utyllity import observer
from widgets.shered.baseView import BaseView


class ImageNavigationView(BaseView):
    def __init__(self, parent: BaseView = None):
        super().__init__(parent)
        self.set_background('#660000')
        self._setup_button()
        self._parent = parent
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._next_in_show)
        self.timer_run = False

    def _setup_button(self):
        self.but_next_collection = QPushButton(self)
        self.but_next_image = QPushButton(self)
        self.but_prev_collection = QPushButton(self)
        self.but_prev_image = QPushButton(self)
        self.but_run_auto = QPushButton(self)
        self.but_tag_for_show = QPushButton(self)

        self.but_prev_image.setText('<<<')
        self.but_next_image.setText('>>>')
        self.but_next_collection.setText('DOWN')
        self.but_prev_collection.setText('UP')
        self.but_run_auto.setText('RUN')
        self.but_tag_for_show.setText('TAG FOR SHOW')

        self.but_prev_image.clicked.connect(self._but_prev_image_action)
        self.but_next_image.clicked.connect(self._but_next_image_action)
        self.but_next_collection.clicked.connect(self._but_next_collection_action)
        self.but_prev_collection.clicked.connect(self._but_prev_collection_action)
        self.but_run_auto.clicked.connect(self._but_run_auto)
        self.but_tag_for_show.clicked.connect(self._but_next_tag_for_show)

    @staticmethod
    def _but_prev_image_action():
        collection_manager.prev_image()
        observer.call_event(EventName.NEW_IMAGE)

    @staticmethod
    def _but_next_image_action():
        collection_manager.next_image()
        observer.call_event(EventName.NEW_IMAGE)

    @staticmethod
    def _but_prev_collection_action():
        collection_manager.prev_collection()
        observer.call_event(EventName.NEW_IMAGE)

    @staticmethod
    def _but_next_collection_action():
        collection_manager.next_collection()
        observer.call_event(EventName.NEW_IMAGE)

    @staticmethod
    def _next_in_show():
        collection_manager.next_in_show()
        observer.call_event(EventName.NEW_IMAGE)

    @staticmethod
    def _but_next_tag_for_show():
        collection_manager.tag_ass_part_of_show()
        observer.call_event(EventName.NEW_IMAGE)

    def _but_run_auto(self):
        if not self.timer_run:
            if collection_manager.start_auto_run():
                self.timer.start(3000)
                self.timer_run = True
                self.but_run_auto.setText('STOP')
                collection_manager.start_auto_run()
        else:
            self.timer_run = False
            self.timer.stop()
            self.but_run_auto.setText('RUN')
            collection_manager.stop_auto_run()

    def resizeEvent(self, a0) -> None:
        super().resizeEvent(a0)

        butt_width = 100

        self.but_next_collection.resize(butt_width, self.size().height())
        self.but_prev_collection.resize(butt_width, self.size().height())
        self.but_next_image.resize(butt_width, self.size().height())
        self.but_prev_image.resize(butt_width, self.size().height())
        self.but_run_auto.resize(butt_width, self.size().height())
        self.but_tag_for_show.resize(butt_width, self.size().height())

        self.but_next_collection.move(butt_width * 0, 0)
        self.but_prev_collection.move(butt_width * 1, 0)
        self.but_prev_image.move(butt_width * 2, 0)
        self.but_next_image.move(butt_width * 3, 0)
        self.but_run_auto.move(butt_width * 4, 0)
        self.but_tag_for_show.move(butt_width * 5, 0)
