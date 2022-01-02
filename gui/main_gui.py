import sys
import os
from pathlib import Path
from api.api import Api
from PySide6.QtCore import QObject, Slot, QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


def run_gui():
    
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    api = Api()

    context = engine.rootContext()
    context.setContextProperty("api", api)

    qml_file = Path(__file__).parent / 'view.qml'
    url = QUrl.fromLocalFile(os.fspath(qml_file.resolve()))
    engine.load(url)

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
