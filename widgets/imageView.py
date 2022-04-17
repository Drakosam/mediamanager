from PyQt6 import QtCore
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QMovie, QImage, QPixmap
from PyQt6.QtWidgets import QLabel

from collection import collection_manager
from widgets.baseView import BaseView


class ImageView(BaseView):
    def __init__(self, parent: BaseView = None):
        self._parent = parent
        super().__init__(parent)
        self.set_background('#000000')
        self.label = QLabel(self)
        self.label.setScaledContents(False)

    def update_image(self):
        image = collection_manager.get_image_path()
        if image == '':
            return

        if '.gif' in image:
            self._update_as_movie(image)
        else:
            self._update_as_image(image)

    def _update_as_image(self, image):
        pix_map = self._get_pix_map_from_image(image)
        self.label.setPixmap(pix_map)
        self.label.move(0, 0)
        if image:
            w_dif = self.size().width() - pix_map.size().width()
            if w_dif > 0:
                self.label.move(int(w_dif / 2), 0)

    def _update_as_movie(self, image):
        self.label.move(0, 0)
        movie = QMovie(image)
        movie.setScaledSize(
            QSize().scaled(self.size().width(), self.size().height(), QtCore.Qt.AspectRatioMode.KeepAspectRatio))
        self.label.setMovie(movie)
        movie.start()
        if image:
            w_dif = self.size().width() - movie.scaledSize().width()
            if w_dif > 0:
                self.label.move(int(w_dif / 2), 0)

    def _get_pix_map_from_image(self, image):
        qmap = QPixmap.fromImage(QImage(image))
        return qmap.scaled(
            self.size().width(),
            self.size().height(),
            QtCore.Qt.AspectRatioMode.KeepAspectRatio,
            transformMode=QtCore.Qt.TransformationMode.SmoothTransformation)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.update_image()
        self.label.resize(self.size())
