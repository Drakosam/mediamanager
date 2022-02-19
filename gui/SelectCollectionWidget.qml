import QtQuick 2.3
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12
import QtQuick.Window 2.12
import QtQuick.Controls.Material 2.12

Item{

    Rectangle{
        anchors.fill: parent
        color: '#000000'

        Rectangle{
            id: imageWidget
            width: parent.width - 300
            height: parent.height
            ImageView{
                anchors.fill: parent
            }
        }
        Rectangle{
            x: parent.width - 300
            width: 300
            height: parent.height
            ImageList{
                anchors.fill: parent
            }
        }
    }
}