
import os
import sys

from   PyQt5.QtWidgets          import * 
from   PyQt5.QtSvg              import * 
from   PyQt5.QtCore             import *
from   PyQt5.QtGui              import * 
from   pathlib                  import Path



def svgIcon(name, size = (64, 64), color = QColor(0,0,0,200)):
	package_folder = Path(__file__).parent
	renderer = QSvgRenderer(os.path.join(package_folder, "ICONS", f"{name}.svg"))
	pixmap   = QPixmap(size[0], size[1])
	pixmap.fill(Qt.GlobalColor.transparent)
	painter  = QPainter(pixmap)
	renderer.render(painter)
	painter.setCompositionMode(painter.CompositionMode.CompositionMode_SourceIn)
	painter.fillRect(pixmap.rect(), color)
	painter.end()
	return QIcon(pixmap)#QPixmap.fromImage(img))

if __name__ == '__main__':
	# import pyqtgraph.examples
	# pyqtgraph.examples.run()
	app     = QApplication(sys.argv)
	svgIcon("table-solid")
	sys.exit(app.exec_())

