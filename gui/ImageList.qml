import QtQuick 2.3
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12
import QtQuick.Window 2.12
import QtQuick.Controls.Material 2.12

Item{
    Connections {
        target: api
        function onCollectionListChanged() {
            refreshList()
        }
    }
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
                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        api.pickCollection(no_item)

                    }
                }
            }
        }

        ListModel {
            id:listModel
            ListElement{
               name:"xxx1"
               no_item:0
            }
        }
    }

    function refreshList(){
        listModel.clear()
        var _collectionList = JSON.parse(api.collectionList)
        for(var i in _collectionList){
            var item = _collectionList[i]
            console.log(item.name,i)
            listModel.append(
                {
                    name:item.name,
                    no_item:item.index
                }
            )
        }
    }
}