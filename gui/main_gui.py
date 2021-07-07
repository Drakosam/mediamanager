import sys
import os
from pathlib import Path

from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

def run_gui():
    
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # bridge = Bridge()

    # context = engine.rootContext()
    # context.setContextProperty("con", bridge)

    qmlFile = Path(__file__).parent / 'view.qml'

    engine.load(os.fspath(qmlFile.resolve()))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())