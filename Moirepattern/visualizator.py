import sys
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtSvg import QSvgRenderer, QGraphicsSvgItem
from PyQt5.QtCore import Qt
import tempfile

def visualize(Moire): 
    
    background = tempfile.NamedTemporaryFile(suffix='.svg', delete=False)
    foreground = tempfile.NamedTemporaryFile(suffix='.svg', delete=False)
    
    Moire.export(background.name)
    Moire.export_base(foreground.name)
    
    app = QApplication(sys.argv)
    scene = QGraphicsScene()

    # Crear objetos QGraphicsSvgItem para los SVG
    item_bg = QGraphicsSvgItem(background.name)
    item_fg = QGraphicsSvgItem(foreground.name)

    # Añadir los QGraphicsSvgItem a la escena
    scene.addItem(item_bg)
    scene.addItem(item_fg)

    # Configurar las banderas para el elemento de primer plano
    item_fg.setFlag(QGraphicsItem.ItemIsMovable)
    item_fg.setFlag(QGraphicsItem.ItemIsSelectable)

    view = QGraphicsView(scene)
    view.show()

    sys.exit(app.exec_())
    background.close()
    foreground.close()