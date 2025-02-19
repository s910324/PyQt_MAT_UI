import os
import sys
from   PyQt5.Qt                 import Qt
from   PyQt5.QtWidgets          import * 
from   PyQt5.QtCore             import *
from   PyQt5.QtGui              import * 
import UI_theme                 as theme
from   UI_elements              import *
from   UI_icon                  import * 

class w(RoundWidget):
	def __init__(self, *args, **argv):
		super().__init__()
		self._label              = RoundLabel("Round Label")
		self._combobox           = RoundComboBox({"Item-1" : "item_1", "Item-2" : "item_2", "Item-3" : "item_3", "Item-4" : "item_4"}).setTheme(theme.rgb_pink)
		self._checkbox           = RoundCheckBox("Check Box").setTheme(theme.rgb_yellow)
		self._pushbutton         = RoundPushButton("Push buttom").setTheme(theme.rgb_orange)
		self._lineedit           = RoundLineEdit("Line edit").setTheme(theme.rgb_violet)
		self._dblspin            = RoundDoubleSpinBox().setTheme(theme.rgb_violet)

		self._label_disable      = RoundLabel("Round Label")
		self._combobox_disable   = RoundComboBox({"Item-1" : "item_1", "Item-2" : "item_2", "Item-3" : "item_3", "Item-4" : "item_4"})
		self._checkbox_disable   = RoundCheckBox("Check Box")
		self._pushbutton_disable = RoundPushButton("Push buttom")
		self._lineedit_disable   = RoundLineEdit("Line edit")
		self._dblspin_disable    = RoundDoubleSpinBox()

		self._pushbutton_icon    = RoundPushButton("icon", icon = svgIcon("trash-can-solid",          size = (12, 12), color = QColor(200, 200, 200, 255)))
		self._pushbutton_small   = RoundPushButton(        icon = svgIcon("trash-can-solid",          size = (12, 12), color = QColor(200, 200, 200, 255))).setTheme(theme.rgb_yellow, ["1px", "3px", "5px", "7px"])

		self._frame              = QGridLayout()
		self._pushbutton_small.setFixedWidth(20)

		disable_group = [
			self._label_disable,      
			self._combobox_disable,   
			self._checkbox_disable,   
			self._pushbutton_disable, 
			self._lineedit_disable,   
			self._dblspin_disable,   
		]

		_= [w.setDisabled(True) for w in disable_group]
 
		self._frame.addWidget(RoundLabel("Label"),        0, 0, 1, 1)
		self._frame.addWidget(RoundLabel("Combo Box"),    1, 0, 1, 1)
		self._frame.addWidget(RoundLabel("Check Box"),    2, 0, 1, 1)
		self._frame.addWidget(RoundLabel("Push Button"),  3, 0, 1, 1)
		self._frame.addWidget(RoundLabel("Line Edit"),    4, 0, 1, 1)
		self._frame.addWidget(RoundLabel("Spin Box"),     5, 0, 1, 1)

		self._frame.addWidget(self._label,                0, 1, 1, 1)
		self._frame.addWidget(self._combobox,             1, 1, 1, 1)
		self._frame.addWidget(self._checkbox,             2, 1, 1, 1)
		self._frame.addWidget(self._pushbutton,           3, 1, 1, 1)
		self._frame.addWidget(self._lineedit,             4, 1, 1, 1)
		self._frame.addWidget(self._dblspin,              5, 1, 1, 1)

		self._frame.addWidget(self._label_disable,        0, 2, 1, 1)
		self._frame.addWidget(self._combobox_disable,     1, 2, 1, 1)
		self._frame.addWidget(self._checkbox_disable,     2, 2, 1, 1)
		self._frame.addWidget(self._pushbutton_disable,   3, 2, 1, 1)
		self._frame.addWidget(self._lineedit_disable,     4, 2, 1, 1)
		self._frame.addWidget(self._dblspin_disable,      5, 2, 1, 1)

		self._frame.addWidget(self._pushbutton_icon,      3, 3, 1, 1)
		self._frame.addWidget(self._pushbutton_small,     3, 4, 1, 1)

		self.setLayout(self._frame)
		
if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	window = w()
	window.show()
	sys.exit(app.exec_())
