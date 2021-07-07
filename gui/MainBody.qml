import QtQuick 2.0
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12
import QtQuick.Window 2.12
import QtQuick.Controls.Material 2.12

Item{
    property var window

    Rectangle{
        anchors.fill: parent
        color: '#000000'

        
        Rectangle{
            y:30
            width:parent.width
            height:parent.height -35
            color: '#444'
        }
        Button {
            x:parent.width - 35
            width:35
            height:35
            text: "✖"
            onClicked: {window.close()}
        }
    }
    function setWindowHandle(handle){
        window = handle
    }
}