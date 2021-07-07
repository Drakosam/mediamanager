import QtQuick.Shapes 1.12
import QtQuick 2.0
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12
import QtQuick.Window 2.12
import QtQuick.Controls.Material 2.12


Item{
    id:itemBorder
    property var window: null
    property var type: 'top'

    MouseArea {
        anchors.fill: parent
        acceptedButtons: Qt.NoButton
        hoverEnabled: true
        cursorShape: {
            return Qt.SizeVerCursor
        }
    }
    Rectangle{
        anchors.fill: parent
        color:'#ff0000'
    }


    DragHandler {
        id: resizeHandler
        grabPermissions: TapHandler.TakeOverForbidden
        target: null
        onActiveChanged: if (active) {
            
            if (type == 'top'){
                window.startSystemResize(Qt.TopEdge);
            }
            else if(type == 'bottom'){
                itemBorder.y = parent.window - 3
                window.startSystemResize(Qt.BottomEdge);
            }
            
        }
    
    }

    function setupWidged(handler,in_type='top'){
        window = handler
        type = in_type
    }
}