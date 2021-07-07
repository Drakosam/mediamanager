import QtQuick.Shapes 1.12
import QtQuick 2.0
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12
import QtQuick.Window 2.12
import QtQuick.Controls.Material 2.12


ApplicationWindow{
    id: window
    visible: true
    flags: Qt.FramelessWindowHint
    width: 640
    height: 480
    title: qsTr("Stack")
    color: "#333333"
    
    


    Rectangle{
        width:parent.width
        height:parent.height-3
        opacity: 0.1

        BorderWidget{
            id:topBorderWidget
            width:parent.width
            height:3
        }
        BorderWidget{
            id:bottomBorderWidget
            width:parent.width
            height:3
            anchors.top:parent.bottom
        }
    }

    Button {
            x:parent.width - 35
            y:3
            width:35
            height:35
            text: "✖"
            onClicked: {window.close()}
    }
    Component.onCompleted: {
        topBorderWidget.setupWidged(window,'top')
        bottomBorderWidget.setupWidged(window,'bottom')
        //mainBody.setWindowHandle(window)
    }
}