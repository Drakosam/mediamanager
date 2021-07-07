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
            if(type == 'top' || type == 'bottom') return Qt.SizeVerCursor
            if(type == 'right' || type == 'left') return Qt.SizeHorCursor
            if(type == 'top-left' || type == 'bottom-right') return Qt.SizeFDiagCursor
            if(type == 'top-right' || type == 'bottom-left') return Qt.SizeBDiagCursor
            if(type == 'move') return Qt.ArrowCursor
        }
    }
    Rectangle{
        anchors.fill: parent
        color:'#000000'
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
                window.startSystemResize(Qt.BottomEdge);
            }
            else if(type == 'right'){
                window.startSystemResize(Qt.RightEdge);
            }
            else if(type == 'left'){
                window.startSystemResize(Qt.LeftEdge);
            }
            else if(type == 'top-left'){
                window.startSystemResize(Qt.TopEdge|Qt.LeftEdge);
            }
            else if(type == 'bottom-right'){
                window.startSystemResize(Qt.BottomEdge|Qt.RightEdge);
            }
            else if(type == 'top-right'){
                window.startSystemResize(Qt.TopEdge|Qt.RightEdge);
            }
            else if(type == 'bottom-left'){
                window.startSystemResize(Qt.BottomEdge|Qt.LeftEdge);
            }
            else if(type == 'move'){
                window.startSystemMove()
            }
        }
    
    }

    function setupWidged(handler,in_type='top'){
        window = handler
        type = in_type
    }
}