
from   PyQt5.Qt                 import Qt
from   PyQt5.QtWidgets          import * 
from   PyQt5.QtCore             import *
from   PyQt5.QtGui              import * 
from   qtwidgets                import AnimatedToggle
import UI_theme                 as theme
import UI_imageres


class RoundLabel(QLabel):
	def __init__(self, *args, **argv):
		super(RoundLabel, self).__init__(*args, **argv)
		self.setTheme()

	def setTheme(self, prime_color = None):
		self._theme_pack = theme.default_theme_pack(prime_color)
		new_theme  = theme.generate_theme(**self._theme_pack) 
		self.setStyleSheet(theme.label_theme(new_theme))
		return self

class RoundCheckBox(QCheckBox):
	valueChanged = pyqtSignal(Qt.CheckState)
	def __init__(self, *args, **argv):
		super(RoundCheckBox, self).__init__(*args, **argv)
		self.setTheme()
		self.stateChanged.connect(lambda val : self.valueChanged.emit(val))	

	def setTheme(self, prime_color = None, theme_pack = None,):
		self._theme_pack = theme.default_theme_pack(prime_color)
		new_theme  = theme.generate_theme(**self._theme_pack) 
		self.setStyleSheet(theme.checkbox_theme(new_theme))
		return self
	
	def updateTheme(self, update_items):
		self.setStyleSheet(theme.checkbox_theme(new_theme))
		return self

class RoundPushButton(QPushButton):
	def __init__(self, *args, **argv):
		super(RoundPushButton, self).__init__(*args, **argv)
		self.setTheme()

	def setTheme(self, prime_color = None, radius = None):
		self._theme_pack = theme.default_theme_pack(prime_color)
		new_theme  = theme.generate_theme(**self._theme_pack) 
		self.setStyleSheet(theme.pushbutton_theme(new_theme, radius))
		return self

class RoundLineEdit(QLineEdit):
	valueChanged = pyqtSignal(str)
	def __init__(self, *args, **argv):
		super(RoundLineEdit, self).__init__( *args, **argv) 
		self.textChanged.connect(lambda val : self.valueChanged.emit(val))
		self.setTheme()

	def setTheme(self, prime_color = None, radius = None):
		self._theme_pack = theme.default_theme_pack(prime_color)
		new_theme  = theme.generate_theme(**self._theme_pack) 
		self.setStyleSheet(theme.lineedit_theme(new_theme, radius))
		return self
		

class RoundComboBox(QComboBox):
	valueChanged = pyqtSignal(int)
	def __init__(self, items, defaultIndex = 0):
		super(RoundComboBox, self).__init__( )
		self.setItems(items, defaultIndex)
		self.setTheme()
		self.currentIndexChanged.connect(lambda val : self.valueChanged.emit(val))

	def setItems(self, items, defaultIndex = 0):
		self.clear()
		self._items = items
		if isinstance(items, list):
			self.addItems(items)
		if isinstance(items, dict):
			self.addItems(items.keys())
		self.setCurrentIndex (defaultIndex)

	def wheelEvent(self, *args, **kwargs):
		pass

	def getDictValue(self):
		if isinstance(self._items, dict):
			return self._items[self.currentText()]
		else:
			raise IndexError("Combobox item is not a dictionary")
		return None

	def setTheme(self, prime_color = None, radius = None):
		self.PopupOffcet = (0, 0)
		self.fade        = True
		self.slide       = False
		self.stretch     = True
		self.lineedit    = QLineEdit()

		self.setLineEdit(self.lineedit)
		self.setEditable(True)
		self.lineEdit().setReadOnly(True)
		self.lineEdit().setAlignment(Qt.AlignCenter)

		self._theme_pack = theme.default_theme_pack(prime_color)
		new_theme  = theme.generate_theme(**self._theme_pack) 
		self.lineedit.setStyleSheet(theme.combobox_edit_theme(new_theme, radius))
		self.setStyleSheet(theme.combobox_list_theme(new_theme))
		return self
		

class RoundDoubleSpinBox(QDoubleSpinBox):
	def __init__(self, min_value:float = 0, max_value:float = 100, default_value = 0, step:float = 1 , decimal:int = 2, ):
		super().__init__()
		self._range_theme_array = []
		
		self.setRange(min_value, max_value)
		self.setSingleStep (step)
		self.setDecimals (decimal)
		self.setValue(default_value)
		self._init_ui()
		self._init_signal()
		self.setTheme()
		

	def _init_ui(self):
		self._range_theme   = ""

	def _init_signal(self):
		self.valueChanged.connect(self._apply_range_theme)

	def value(self):
		return round(super(RoundDoubleSpinBox, self).value(), self.decimals() + 1)

	def wheelEvent(self, *args, **kwargs):
		pass

	def addRangeTheme(self, functon, fg_color_rgba = None, bg_color_rgba = None, text_style = None):
		self._range_theme_array.append([functon, fg_color_rgba, bg_color_rgba, text_style])
		self._update_range_theme()

	def _update_range_theme(self):
		theme_style_list = []
		unpack = lambda list_item : ", ".join([ str(i) for i in list_item])

		for theme_id, theme in enumerate(self._range_theme_array):
			function, fg_color_rgba, bg_color_rgba, text_style = theme

			unit_style = "\n".join([t for t in[
				f"	color      :rgba({unpack(fg_color_rgba)});" if fg_color_rgba else "",
				f"	background :rgba({unpack(bg_color_rgba)});" if bg_color_rgba else "",
			] if t])

			if unit_style:
				theme_style = f"""QDoubleSpinBox[range_theme_{theme_id}=True] {{\n{unit_style}\n}}"""
				theme_style_list.append(theme_style)

		self._range_theme = "\n".join(theme_style_list)
		self.setTheme()


	def _apply_range_theme(self):
		for theme_id, theme in enumerate(self._range_theme_array):
			function, *_ = theme

			try:
				self.setProperty(f"range_theme_{theme_id}", str(function(self.value())))

			except Exception as e:
				print ( f"RoundDoubleSpinBox range theme error : {self.value()}")
		
		self.style().unpolish(self)
		self.style().polish(self)

	def setTheme(self, prime_color = None):
		self._theme_pack = theme.default_theme_pack(prime_color)
		new_theme  = theme.generate_theme(**self._theme_pack) 
		self.setAlignment(Qt.AlignHCenter)
		self.setStyleSheet(theme.dblspin_theme(new_theme) + self._range_theme)
		return self

class RoundListWidget(QListWidget):
	def __init__(self):
		super(RoundListWidget, self).__init__()
		self.setTheme()
		self.setDropIndicatorShown(True)
		self.setDragDropMode(QAbstractItemView.InternalMove)
		self.setDefaultDropAction(Qt.MoveAction)

	def setTheme(self, prime_color = None):
		self.setFrameShadow(QFrame.Plain)
		self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
		self.setStyleSheet(theme.list_theme(new_theme))
		return self


class RoundMainWindow(QMainWindow):
	def __init__(self):
		super(RoundMainWindow, self).__init__()
		self.setTheme()

	def setTheme(self, prime_color = None):
		self._theme_pack = theme.default_theme_pack(prime_color)
		new_theme  = theme.generate_theme(**self._theme_pack) 
		self.setStyleSheet(theme.mainwindow_theme(new_theme))
		return self

class RoundWidget(QWidget):
	def __init__(self):
		super(RoundWidget, self).__init__()
		self._theme_pack = None
		self.setTheme()

	def setTheme(self, prime_color = None):
		self._theme_pack = theme.default_theme_pack(prime_color)
		new_theme  = theme.generate_theme(**self._theme_pack) 
		self.setStyleSheet(theme.widget_theme(new_theme))
		return self

class QLine(QFrame):
	def __init__(self):
		super(QLine, self).__init__()
		self.setFrameShape(QFrame.VLine)
		self.setFrameShadow(QFrame.Plain)
		line_theme = """
			QFrame {
				color: rgba(5, 5, 5, 200);
			}
		"""
		self.setStyleSheet(line_theme)

class QVLine(QLine):
	def __init__(self):
		super(QVLine, self).__init__()
		self.setFrameShape(QFrame.VLine)

class QHLine(QLine):
	def __init__(self):
		super(QHLine, self).__init__()
		self.setFrameShape(QFrame.HLine)
