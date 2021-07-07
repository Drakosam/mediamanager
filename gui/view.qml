import QtQuick.Shapes 1.12
import QtQuick 2.0
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12
import QtQuick.Window 2.12
import QtQuick.Controls.Material 2.12


ApplicationWindow{
    id: window
    visible: true
    flags: Qt.FramelessWindowHint| Qt.Window
    width: 640
    height: 480
    title: qsTr("Stack")
    color: "#333333"
    property var frameSize : 5

    Rectangle{
        width:parent.width
        height:parent.height-frameSize

        BorderWidget{
            id:topBorderWidget
            width:parent.width
            height:frameSize
        }
        BorderWidget{
            id:bottomBorderWidget
            width:parent.width
            height:frameSize
            anchors.top:parent.bottom
        }
        BorderWidget{
            id:leftBorderWidget
            width:frameSize
            height:parent.height
        }
        BorderWidget{
            id:rightBorderWidget
            x:parent.width - frameSize
            width:frameSize
            height:parent.height
        }
        BorderWidget{
            id:topLeftBorderWidget
            width:30
            height:30
        }
        BorderWidget{
            id:bottomRightBorderWidget
            x:parent.width - 30
            y:parent.height - 30
            width:30
            height:30
        }
        BorderWidget{
            id:topRightBorderWidget
            x:parent.width - 30
            width:30
            height:30
        }
        BorderWidget{
            id:bottomLeftBorderWidget
            y:parent.height - 30
            width:30
            height:30
        }
        BorderWidget{
            id:moveBarWidget
            y:frameSize
            x:frameSize
            height:35
            width:parent.width - frameSize - frameSize
        }
    }
    MainBody{
        id:mainBody
        x:frameSize
        y:frameSize
        height:parent.height - frameSize - frameSize
        width:parent.width - frameSize - frameSize
    }
    Component.onCompleted: {
        topBorderWidget.setupWidged(window,'top')
        bottomBorderWidget.setupWidged(window,'bottom')
        leftBorderWidget.setupWidged(window,'left')
        rightBorderWidget.setupWidged(window,'right')
        topLeftBorderWidget.setupWidged(window,'top-left')
        bottomRightBorderWidget.setupWidged(window,'bottom-right')
        topRightBorderWidget.setupWidged(window,'top-right')
        bottomLeftBorderWidget.setupWidged(window,'bottom-left')
        moveBarWidget.setupWidged(window,'move')
        mainBody.setWindowHandle(window)
    }
}