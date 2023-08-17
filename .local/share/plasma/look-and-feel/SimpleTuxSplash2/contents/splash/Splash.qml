import QtQuick 2.5


Rectangle {
    id: root
    color: "#0e0e0e"

    property int stage

    onStageChanged: {
        if (stage == 1) {
            introAnimation.running = true
        }
    }


    Item {
        id: content
        anchors.fill: parent
        opacity: 0
        TextMetrics {
            id: units
            text: "M"
            property int gridUnit: boundingRect.height
            property int largeSpacing: units.gridUnit
            property int smallSpacing: Math.max(2, gridUnit/4)
        }

        Image {
            id: logo
            //match SDDM/lockscreen avatar positioning
            property real size: units.gridUnit * 8

            anchors.centerIn: parent

            source: "images/tux.png"

            sourceSize.width: size
            sourceSize.height: size


       AnimatedSprite {
           id: anim0
           width: 42  // Ancho del sprite (total hacia la derecha)
           height: 9 // Altura del cuadro
           frameWidth: 42
           frameHeight: 9

           anchors {
               bottom: parent.bottom
               bottomMargin: -40
               horizontalCenter: parent.horizontalCenter
           }

           frameDuration: 400
           source: "images/busysprite03.png"
           frameCount: 6 // Cuadros verticales
           running: true
           }
      }
    }

    OpacityAnimator {
        id: introAnimation
        running: false
        target: content
        from: 0
        to: 1
        duration: 1000
        easing.type: Easing.InOutQuad
    }
}
