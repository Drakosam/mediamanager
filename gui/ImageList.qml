import QtQuick 2.3
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12
import QtQuick.Window 2.12
import QtQuick.Controls.Material 2.12

Item{
    Rectangle{
        anchors.fill: parent
        color: '#aaaaaa'

        ListModel {
            anchors.fill: parent
            id:listModel

            ListElement{
               name:xxx
            }
            ListElement{
               name:xxx1
            }
            ListElement{
               name:xxx2
            }
            ListElement{
               name:xxx3
            }
            ListElement{
               name:xxx4
            }
        }
    }
}