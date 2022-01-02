import QtQuick 2.3
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12
import QtQuick.Window 2.12
import QtQuick.Controls.Material 2.12

Item{
    Rectangle{
        id:listArea
        anchors.fill: parent
        color: '#aaaaaa'

        ListView{
            anchors.fill: parent
            model:listModel
            displayMarginBeginning: -10
            delegate:Rectangle{
                height: 40
                width:listArea.width
                border.color: "black"
                border.width: 1
                Text{
                    anchors.fill: parent
                    text:name
                    horizontalAlignment:Text.AlignHCenter
                    verticalAlignment:Text.AlignVCenter
                    wrapMode:Text.WrapAnywhere
                }
            }
        }

        ListModel {
            id:listModel
            ListElement{
               name:"xxx1"
            }
            ListElement{
               name:"Lorem ipsum dolor sit amet, consectetur adipiscing elit"
            }
            ListElement{
               name:"Lorem ipsum dolor sit amet, consectetur adipiscing elit"
            }
            ListElement{
               name:"Lorem ipsum dolor sit amet, consectetur adipiscing elit"
            }
            ListElement{
               name:"Lorem ipsum dolor sit amet, consectetur adipiscing elit"
            }
            ListElement{
               name:"Lorem ipsum dolor sit amet, consectetur adipiscing elit"
            }
            ListElement{
               name:"Lorem ipsum dolor sit amet, consectetur adipiscing elit"
            }
            ListElement{
               name:"Lorem ipsum dolor sit amet, consectetur adipiscing elit"
            }
            ListElement{
               name:"Lorem ipsum dolor sit amet, consectetur adipiscing elit"
            }
            ListElement{
               name:"Lorem ipsum dolor sit amet, consectetur adipiscing elit"
            }
            ListElement{
               name:"Lorem ipsum dolor sit amet, consectetur adipiscing elit"
            }
            ListElement{
               name:"Lorem ipsum dolor sit amet, consectetur adipiscing elit"
            }
            ListElement{
               name:"Lorem ipsum dolor sit amet, consectetur adipiscing elit"
            }
            ListElement{
               name:"Lorem ipsum dolor sit amet, consectetur adipiscing elit"
            }
            ListElement{
               name:"Lorem ipsum dolor sit amet, consectetur adipiscing elit"
            }
            ListElement{
               name:"Lorem ipsum dolor sit amet, consectetur adipiscing elit"
            }
            ListElement{
               name:"xxx2"
            }
            ListElement{
               name:"xxx3"
            }
            ListElement{
               name:"xxx4"
            }
        }
    }
}