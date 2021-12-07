import QtQuick 2.3
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12
import QtQuick.Window 2.12
import QtQuick.Controls.Material 2.12

Item{
    property var window
    property var maxi:false
    Rectangle{
        id:mainBody
        anchors.fill: parent
        color: '#000000'

        ColumnLayout{
            anchors.fill: parent
            spacing: 1
            Rectangle{
                Layout.preferredWidth: mainBody.width
                Layout.preferredHeight: 35
                color: '#222'

                RowLayout {
                    id: layout
                    anchors.fill: parent
                    spacing: 1
                    Button {
                        id:layoutButton1
                        width:100
                        height:25
                        text: "images"
                        Layout.alignment: Qt.AlignLeft
                        onClicked: {swipeView.currentIndex = 0}
                    }
                    Button {
                        id:layoutButton2
                        anchors.left: layoutButton1.right
                        width:100
                        height:25
                        text: "collection"
                        Layout.alignment: Qt.AlignLeft
                        onClicked: {swipeView.currentIndex = 1}
                    }
                    Button {
                        id:layoutButton3
                        anchors.left: layoutButton2 .right
                        width:100
                        height:25
                        text: "settings"
                        Layout.alignment: Qt.AlignLeft
                        onClicked: {swipeView.currentIndex = 2}
                    }
                }
            }
            Rectangle{
                Layout.fillHeight: true
                Layout.preferredWidth: parent.width
                Layout.preferredHeight: parent.height
                color: '#000'
                SwipeView {
                        id: swipeView
                        currentIndex: 0
                        anchors.fill: parent

                        Item {
                            id: firstPage
                            Rectangle{
                                anchors.fill: parent
                                color: '#000'
                                SelectCollectionWidget{
                                    anchors.fill: parent
                                }
                            }
                        }
                        Item {
                            id: secondPage
                            Rectangle{
                                anchors.fill: parent
                                color: '#0f0'
                            }
                        }
                        Item {
                            id: thirdPage
                            Rectangle{
                                anchors.fill: parent
                                color: '#00f'
                            }
                        }
                }
            }
        }
        Button {
            x:parent.width - 35
            width:35
            height:25
            text: "✖"
            onClicked: {window.close()}
        }
        Button {
            x:parent.width - 35 - 37
            width:35
            height:25
            text: "▣"
            onClicked: {
                if(maxi){
                    window.showNormal()
                }else{
                    window.showMaximized()
                }
                maxi = !maxi
            }
        }
    }
    function setWindowHandle(handle){
        window = handle
    }
}