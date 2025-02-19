import sys
from   PyQt5.Qt                 import Qt
from   PyQt5.QtWidgets          import * 
from   PyQt5.QtCore             import *
from   PyQt5.QtGui              import * 
from   qtwidgets                import AnimatedToggle
import UI_theme                 as theme
from   UI_elements              import *
from   UI_icon                  import * 
import UI_imageres


class CardSection(RoundWidget):
	def __init__(self, *args, **argv):
		super(CardSection, self).__init__(*args, **argv)
		self.setAttribute(Qt.WA_StyledBackground, True)



class CardHeader(CardSection):
	colapse = pyqtSignal()
	
	def __init__(self, *args, **argv):
		super(CardHeader, self).__init__(*args, **argv)
		colapse_svg = svgIcon("caret-down-solid",size = ( 8,  8), color = QColor(200, 200, 200, 255))
		remove_svg  = svgIcon("trash-can-solid", size = (10, 10), color = QColor(200, 200, 200, 255))
		self._colapse_pb = RoundPushButton(icon = colapse_svg).setTheme(theme.rgb_light_grey, ["5px", "0px", "0px", "0px"])
		self._remove_pb  = RoundPushButton(icon = remove_svg ).setTheme(theme.rgb_light_grey, ["0px", "5px", "0px", "0px"])
		self._title_pb   = RoundPushButton("title, 123").setTheme(theme.rgb_light_grey, ["0px", "0px", "0px", "0px"])
		self._frame      = QGridLayout()
		self._frame.setContentsMargins(0, 0, 0, 0)
		self._frame.setSpacing(0)
		self._colapse_pb.setFixedSize(25, 25)
		self._title_pb.setFixedHeight(25)
		self._remove_pb.setFixedSize(25, 25)

		self._frame.addWidget(self._colapse_pb, 0, 0, 1, 1)
		self._frame.addWidget(self._title_pb,   0, 1, 1, 1)
		self._frame.addWidget(self._remove_pb,  0, 2, 1, 1)
		
		self._frame.setColumnStretch(0, 0)
		self._frame.setColumnStretch(1, 1)
		self._frame.setColumnStretch(2, 0)
		self.setLayout(self._frame)

		style = """
			
			border-top-left-radius : 5px;
			border-top-right-radius: 5px;
		"""
		self.setStyleSheet(style)
		self.setFixedHeight(25)
		self._init_signal()
		
	def _init_signal(self):
		self._colapse_pb.clicked.connect(lambda : self.colapse.emit())

class CardBody(CardSection):
	def __init__(self, *args, **argv):
		super(CardBody, self).__init__(*args, **argv)
		self.setStyleSheet('background-color: #424242')
		# self.setFixedHeight(200)

	def colapse(self):
		self.setVisible(not(self.isVisible()))

class CardFooter(CardSection):
	def __init__(self, *args, **argv):
		super(CardFooter, self).__init__(*args, **argv)
		style = """
			background-color: #BABABA;
			border-bottom-left-radius : 5px;
			border-bottom-right-radius: 5px;
		"""
		self.setStyleSheet(style)
		self.setFixedHeight(10)

class RoundCard(QWidget):
	def __init__(self, *args, **argv):
		super(RoundCard, self).__init__(*args, **argv)
		self._header = CardHeader()
		self._body   = CardBody()
		self._footer = CardFooter()
		self._frame  = QGridLayout()
		self._frame.setSpacing(0)
		self._frame.addWidget(self._header, 0, 0, 1, 1)
		self._frame.addWidget(self._body,   1, 0, 1, 1)
		self._frame.addWidget(self._footer, 2, 0, 1, 1)
		self._frame.setRowStretch(0, 0)
		self._frame.setRowStretch(1, 1)
		self._frame.setRowStretch(2, 0)
		self.setLayout(self._frame)
		self._init_signal()

	def _init_signal(self):
		self._header.colapse.connect(lambda : self._body.colapse())

if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	window = RoundCard()
	window.show()
	sys.exit(app.exec_())
