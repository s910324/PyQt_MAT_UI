color_tint      = lambda      value, tint : int(sorted([0, (value+tint)/100*255 , 255])[1])
rgb_tint        = lambda rgb_array,  tint : "rgb({0}, {1}, {2})".format(*[color_tint(c, tint) for c in rgb_array])
rgb_white       = [100, 100, 100]
rgb_light_grey  = [ 80,  80,  80]
rgb_red         = [ 85,  15,  15]
rgb_orange      = [ 94,  44,  10]
rgb_yellow      = [ 98,  74,   3]
rgb_olive       = [ 70,  80,   9]
rgb_green       = [ 12,  72,  27]
rgb_teal        = [  0,  70,  67]
rgb_blue        = [  0,  70,  67]
rgb_violet      = [ 39,  20,  78]
rgb_purple      = [ 63,  20,  78]
rgb_pink        = [ 87,  20,  58]
rgb_brown       = [ 64,  40,  24]
rgb_grey        = [ 46,  46,  46]
rgb_black       = [ 10,  10,  11]

main_height     = "18px"
pad_no          = "0.0em"
pad_small       = "0.2em"
pad_mid         = "0.5em"
pad_large       = "0.8em"
pad_huge        = "1.1em"

color_white_100 =  rgb_tint(rgb_white,   0)
color_white_085 =  rgb_tint(rgb_white, -15)
color_white_070 =  rgb_tint(rgb_white, -30)
color_white_055 =  rgb_tint(rgb_white, -45)
color_white_040 =  rgb_tint(rgb_white, -60)
color_white_025 =  rgb_tint(rgb_white, -85)
color_white_010 =  rgb_tint(rgb_white, -90)

light_75_tint   = +75
light_50_tint   = +50
light_25_tint   = +25 
light_10_tint   = +10
light_05_tint   =  +5
dark_main_tint  = -20
light_main_tint =   0
dark_05_tint    =  -5
dark_10_tint    = -10
dark_25_tint    = -25
dark_50_tint    = -50
dark_75_tint    = -75

def dark_theme_pack(prime_color = None):
	prime_color = prime_color if prime_color else rgb_olive
	base_tint   = dark_main_tint + dark_50_tint
	prime_tint  = dark_main_tint + dark_25_tint
	

	return {
		"base_color"               : "#333333",
		"prime_color"              : prime_color,

		"text_active_rgb"          : color_white_085,
		"text_deep_rgb"            : color_white_100,
		"text_disable_rgb"         : color_white_040,

		"reverse_text_active_rgb"  : color_white_040,
		"reverse_text_deep_rgb"    : color_white_025,
		"reverse_text_disable_rgb" : color_white_085,

		"prime_active_rgb"         : rgb_tint(prime_color, prime_tint),
		"prime_hover_rgb"          : rgb_tint(prime_color, prime_tint + light_05_tint),
		"prime_press_rgb"          : rgb_tint(prime_color, prime_tint + dark_05_tint ),
		"prime_disable_rgb"        : rgb_tint(  rgb_white, prime_tint + light_25_tint),
		"prime_select_rgb"         : rgb_tint(   rgb_teal, prime_tint + light_25_tint),
	       
		"base_active_rgb"          : rgb_tint(  rgb_white, base_tint),
		"base_hover_rgb"           : rgb_tint(  rgb_white, base_tint  + light_05_tint),
		"base_press_rgb"           : rgb_tint(  rgb_white, base_tint  + dark_05_tint ),
		"base_disable_rgb"         : rgb_tint(  rgb_white, base_tint  + light_25_tint),
	}

def light_theme_pack(prime_color = None):
	prime_color = prime_color if prime_color else rgb_olive
	base_tint   = light_main_tint + light_25_tint
	prime_tint  = light_main_tint + light_10_tint
	

	return {
		"base_color"               : "#F0F0F0",
		"prime_color"              : prime_color,

		"text_active_rgb"          : color_white_025,
		"text_deep_rgb"            : color_white_010,
		"text_disable_rgb"         : color_white_070,

		"reverse_text_active_rgb"  : color_white_085,
		"reverse_text_deep_rgb"    : color_white_100,
		"reverse_text_disable_rgb" : color_white_040,

		"prime_active_rgb"         : rgb_tint(prime_color, prime_tint),
		"prime_hover_rgb"          : rgb_tint(prime_color, prime_tint + light_05_tint),
		"prime_press_rgb"          : rgb_tint(prime_color, prime_tint + dark_05_tint ),
		"prime_disable_rgb"        : rgb_tint(  rgb_white, prime_tint + light_25_tint),
		"prime_select_rgb"         : rgb_tint(   rgb_teal, prime_tint + light_25_tint),
	       
		"base_active_rgb"          : rgb_tint(  rgb_white, base_tint),
		"base_hover_rgb"           : rgb_tint(  rgb_white, base_tint  + light_05_tint),
		"base_press_rgb"           : rgb_tint(  rgb_white, base_tint  + dark_05_tint ),
		"base_disable_rgb"         : rgb_tint(  rgb_white, base_tint  + light_25_tint),
	}

def generate_theme(
	base_color,	prime_color, 
	text_active_rgb, text_deep_rgb, text_disable_rgb, 
	reverse_text_active_rgb, reverse_text_deep_rgb, reverse_text_disable_rgb, 
	prime_active_rgb, prime_hover_rgb, prime_press_rgb, prime_disable_rgb, prime_select_rgb, base_active_rgb, 
	base_hover_rgb, base_press_rgb, base_disable_rgb):

	return {
		"widget_bg_color"                  : base_color,
		"label_text_color"                 : text_active_rgb,
		"label_text_color_disable"         : text_disable_rgb,
		"label_text_padding"               : "{pad_mid} {pad_no} {pad_mid} {pad_no}",

		"checkbox_text_color"              : text_active_rgb,
		"checkbox_text_color_disable"      : text_disable_rgb,
		"checkbox_text_padding"            : "{pad_mid} {pad_no} {pad_mid} {pad_no}",
		"checkbox_select_color"            : prime_select_rgb, 

		"pushbutton_text_color"            : text_active_rgb,
		"pushbutton_text_color_disable"    : text_disable_rgb,
		"pushbutton_text_padding"          : "{pad_small} {pad_small} {pad_small} {pad_small}",
		"pushbutton_bg_color"              : prime_active_rgb,
		"pushbutton_bg_color_hover"        : prime_hover_rgb,
		"pushbutton_bg_color_press"        : prime_press_rgb,
		"pushbutton_bg_color_disable"      : prime_disable_rgb,

		
		"lineedit_text_color"              : text_active_rgb,
		"lineedit_text_color_disable"      : text_disable_rgb,
		"lineedit_text_padding"            : "{pad_small} {pad_small} {pad_small} {pad_small}",
		"lineedit_select_color"            : prime_select_rgb,
		"lineedit_bg_color"                : base_active_rgb,
		"lineedit_bg_color_hover"          : base_hover_rgb,
		"lineedit_bg_color_press"          : base_press_rgb,
		"lineedit_bg_color_disable"        : base_disable_rgb,

		"dblspin_text_color"               : text_active_rgb,
		"dblspin_text_color_disable"       : text_disable_rgb,
		"dblspin_text_padding"             : "{pad_small} {pad_small} {pad_small} {pad_small}",
		"dblspin_bg_color"                 : base_active_rgb,
		"dblspin_bg_color_disable"         : base_disable_rgb,
		"dblspin_select_color"             : prime_select_rgb, 

		"dblspin_btn_color"                : prime_active_rgb,
		"dblspin_btn_color_disable"        : prime_disable_rgb,
		"dblspin_btn_color_hover"          : prime_hover_rgb,
		"dblspin_btn_color_press"          : prime_press_rgb,


		"combobox_padding"                 : "{pad_small} {pad_small} {pad_small} {pad_small}",
		"combobox_bg_color"                : base_active_rgb,
		"combobox_bg_color_disable"        : base_disable_rgb,

		"combobox_drop_bg_color_hover"     : base_hover_rgb,
		"combobox_drop_bg_color_on"        : base_active_rgb,
		"combobox_drop_padding"            : "{pad_small} {pad_small} {pad_mid} {pad_small}",

		"combobox_edit_text_color"         : text_active_rgb,
		"combobox_edit_text_color_disable" : text_disable_rgb,
		"combobox_edit_padding"            : "{pad_no} {pad_no} {pad_no} {pad_no}",
		"combobox_edit_bg_color"           : "transparent",
		"combobox_edit_select_color"       : prime_select_rgb,
		
		"combobox_list_text_color"         : text_active_rgb,
		"combobox_list_padding"            : "{pad_small} {pad_small} {pad_small} {pad_small}",
		"combobox_list_bg_color"           : base_active_rgb,
		"combobox_list_bd_color"           : text_disable_rgb,

		"combobox_list_text_color_hover"   : reverse_text_deep_rgb,
		"combobox_list_text_color_select"  : reverse_text_deep_rgb,
		"combobox_list_bg_color_hover"     : base_hover_rgb,
		"combobox_list_bg_color_select"    : base_press_rgb,
		"combobox_list_select_color"       : prime_select_rgb,

	}

default_theme_pack = light_theme_pack
default_theme      = generate_theme(**default_theme_pack())

def label_theme(theme = None):
	theme = theme if theme else default_theme
	return f"""
		QLabel {{
			color   : {theme['label_text_color']};
			padding : {theme['label_text_padding']};
			height  : {main_height};
		}}

		QLabel:disabled {{
			color: {theme['label_text_color_disable']};
		}}
	"""

def checkbox_theme(theme = None):
	theme = theme if theme else default_theme
	return f"""
		QCheckBox {{
			color   : {theme['checkbox_text_color']};
			padding : {theme['checkbox_text_padding']};
			height  : {main_height};
			selection-background-color:{theme['checkbox_select_color']};
		}}

		QCheckBox:disabled {{
			color   : {theme['checkbox_text_color_disable']};
		}}
	"""

def pushbutton_theme(theme = None, radius = None):

	theme = theme if theme else default_theme
	radius = radius if radius else ["3px", "3px", "3px", "3px"]


	return f"""
		QPushButton {{
			border-style     : solid;
			border-width     : 0px;
			width            : 60px;
			height           : {main_height};
			color            : {theme['pushbutton_text_color']};
			padding          : {theme['pushbutton_text_padding']};
			background-color : {theme['pushbutton_bg_color']};
			border-top-left-radius     : {radius[0]};
			border-top-right-radius    : {radius[1]};
			border-bottom-left-radius  : {radius[2]};
			border-bottom-right-radius : {radius[3]};
		}}

		QPushButton:hover {{
			background-color : {theme['pushbutton_bg_color_hover']};
		}}
		 
		QPushButton:pressed {{
			background-color : {theme['pushbutton_bg_color_press']};
		}}

		QPushButton:disabled {{
			color            : {theme['pushbutton_text_color_disable']};
			background-color : {theme['pushbutton_bg_color_disable']};
		}}

		QPushButton[warning='true'] {{
			background-color: rgba(240, 140, 0, 120);
		}}
		QPushButton[warning='true']:hover {{
			background-color: rgba(240, 140, 0, 90);
		}}
		QPushButton[warning='true']:pressed {{
			background-color: rgba(240, 140, 0, 60);
		}}
	"""

def lineedit_theme(theme = None, radius = None):
	theme = theme if theme else default_theme
	radius = radius if radius else ["3px", "3px", "3px", "3px"]
	return f"""
		QLineEdit {{
			color            : {theme['lineedit_text_color']};
			padding          : {theme['lineedit_text_padding']};
			background-color : {theme['lineedit_bg_color']};
			selection-background-color:{theme['lineedit_select_color']};
			border-style     : solid;
			border-width     : 0px;
			height           : {main_height};
			width: 60px;
			border-top-left-radius     : {radius[0]};
			border-top-right-radius    : {radius[1]};
			border-bottom-left-radius  : {radius[2]};
			border-bottom-right-radius : {radius[3]};
		}}

		QLineEdit:hover {{
			background-color : {theme['lineedit_bg_color_hover']};
		}}
		 
		QLineEdit:pressed {{
			background-color : {theme['lineedit_bg_color_press']};
		}}

		QLineEdit:disabled {{
			color            : {theme['lineedit_text_color_disable']};
			background-color : {theme['lineedit_bg_color_disable']};
		}}
	"""

def dblspin_theme (theme = None):
	theme = theme if theme else default_theme
	return f"""
		QDoubleSpinBox {{
			color            : {theme['dblspin_text_color']};
			padding          : {theme['dblspin_text_padding']};
			background-color : {theme['dblspin_bg_color']};
			border-style: none;
			border-radius: 3px;
			width: 60px;
			height: {main_height};
			selection-background-color:{theme['dblspin_select_color']};
		}}

		QDoubleSpinBox:disabled{{
			color            : {theme['dblspin_text_color_disable']};
			background-color : {theme['dblspin_bg_color_disable']};
		}}

		QDoubleSpinBox::down-button, QDoubleSpinBox::up-button {{
			subcontrol-origin: margin;
			background-color : {theme['dblspin_btn_color']};
			width: 15px;
			height: 15px;
		}}

		QDoubleSpinBox::down-button:disabled, QDoubleSpinBox::up-button:disabled {{
			background-color : {theme['dblspin_btn_color_disable']};
		}}

		QDoubleSpinBox::down-button {{
			subcontrol-position: center left;
			margin-left: 3px;
		}}
		 
		QDoubleSpinBox::up-button {{
			subcontrol-position: center right;
			margin-right: 3px;
		}}
		 
		QDoubleSpinBox::down-button,
		QDoubleSpinBox::up-button {{
			border-radius: 3px;
		}}
		 
		QDoubleSpinBox::down-button:hover, QDoubleSpinBox::up-button:hover {{
			background-color : {theme['dblspin_btn_color_hover']};
		}}
		 
		QDoubleSpinBox::down-button:pressed,
		QDoubleSpinBox::up-button:pressed {{
			background-color : {theme['dblspin_btn_color_press']};
		}}
		 
		QDoubleSpinBox::up-arrow, QDoubleSpinBox::down-arrow {{
			subcontrol-origin: content;
			width: 10px;
			height: 10px;
		}}
		 
		QDoubleSpinBox::up-arrow{{
			image: url(":/icons/QSpinBox/plus-fill_hover.png");
		}}
		 
		QDoubleSpinBox::down-arrow{{
			image: url(":/icons/QSpinBox/minus-fill_hover.png");
		}}

		QDoubleSpinBox::up-arrow:disabled {{
			image: url(":/icons/QSpinBox/plus-fill_hover.png");
		}}
		 
		QDoubleSpinBox::down-arrow:disabled {{
			image: url(":/icons/QSpinBox/minus-fill_hover.png");
		}}
	"""

def combobox_edit_theme(theme = None, radius = None):
	theme  = theme if theme else default_theme
	radius = radius if radius else ["3px", "3px", "3px", "3px"]
	return f"""
		QLineEdit {{
			color            : {theme['combobox_edit_text_color']};
			padding          : {theme['combobox_edit_padding']};
			background-color : {theme['combobox_edit_bg_color']};
			border-top-left-radius     : {radius[0]};
			border-top-right-radius    : {radius[1]};
			border-bottom-left-radius  : {radius[2]};
			border-bottom-right-radius : {radius[3]};
			selection-background-color:{theme['combobox_edit_select_color']};
		}}

		QLineEdit:disabled  {{
			color            : {theme['combobox_edit_text_color_disable']};
		}}
	"""

def combobox_list_theme(theme = None):
	theme = theme if theme else default_theme
	return f"""
		QComboBox {{
			background-color : {theme['combobox_bg_color']};
			padding          : {theme['combobox_padding']};
			border-style     : solid;
			border-width     : 0px;
			border-radius    : 3px;
			width            : 60px;
			height           : {main_height};
		}}

		QComboBox:disabled {{
			background-color : {theme['combobox_bg_color_disable']};
		}}

		QComboBox::drop-down {{
			padding          : {theme['combobox_drop_padding']};
			image            : url(":/icons/QComboBox/drop-arrow.png");
			width            : 10px;
			height           : {main_height};
			border-top-right-radius   : 3px;
			border-bottom-right-radius: 3px;
		}}
		 
		QComboBox::drop-down:hover {{
			background-color : {theme['combobox_drop_bg_color_hover']};
			image: url(":/icons/QComboBox/drop-arrow_hover.png");
			
		}}
		 
		QComboBox::drop-down:on {{
			background-color : {theme['combobox_drop_bg_color_on']};
			image: url(":/icons/QComboBox/drop-up-arrow.png");
			
			border-bottom-right-radius: 0px;
			border-bottom-left-radius : 0px;
		}}
		 
		QComboBox:on {{
			border-bottom-right-radius: 0px;
			border-bottom-left-radius: 0px;
		}}

		QListView {{
			color            : {theme['combobox_list_text_color']};
			padding          : {theme['combobox_list_padding']};
			background-color : {theme['combobox_list_bg_color']};
			background-color : {theme['combobox_list_bd_color']};
			outline          : none;
			border-style     : solid;

			border-bottom-right-radius : 3px;
			border-bottom-left-radius  : 3px;
			selection-background-color:{theme['combobox_list_select_color']};
		}}

		QListView::item {{
			padding          : {theme['combobox_list_padding']};
			border-style     : solid transparent;
			border-bottom-right-radius: 3px;
			border-bottom-left-radius : 3px;
			selection-background-color:{theme['combobox_list_select_color']};
		}}
		 
		QListView::item:hover{{
			color            : {theme['combobox_list_text_color_hover']};
			background-color : {theme['combobox_list_bg_color_hover']};
		}}

		QListView::item:selected {{
			color            : {theme['combobox_list_text_color_select']};
			background-color : {theme['combobox_list_bg_color_select']};
		}}
	"""

def list_theme(theme = None):
	theme = theme if theme else default_theme
	return f"""
		QListWidget {{
			background-color: #101510;
			padding: 0.2em 0.2em 0.2em 0.2em;
			border-style: solid;
			border-width: 1px;
			border-color: #081008;
			border-radius: 3px;
		}}

		QListWidget:disabled {{
			background-color: #151515;
		}}

		QListWidget::item {{ 
			background: #212121; 
			border-style: solid;
			border-width: 0px;
			border-radius: 3px;
			margin: 0.3em 0.6em 0.3em 0.3em;
		}}

		QListWidget::item:hover {{ 
			background: #282828; 
			border-style: solid;
			border-width: 0px;
			border-radius: 3px;
			margin: 0.3em 0.6em 0.3em 0.3em;
		}}

		QListWidget::item:selected {{ 
			background: #282828; 
			border-style: solid;
			border-width: 0px;
			border-radius: 3px;
			margin: 0.3em 0.6em 0.3em 0.3em; 
		}}

		QScrollBar::groove {{ 
			background-color: rgba(0,0,0,0);
			height: 1px; 
		}}

		QScrollBar::handle {{ 
			height: 2px;
		}}
	"""

def mainwindow_theme(theme = None):
	theme = theme if theme else default_theme
	return f"""
		QDockWidget, MainTestWindow, QMdiSubWindow {{
			background-color: #101210;
		}}

		QDockWidget {{ 
			color : #ddd;
		}}

		QDockWidget::title {{ 
			border: 1px solid #000;
			background-color: #000;
			padding: 0.5em 0.1em 0.1em 0.5em;
		}}

		QTabBar:tab {{ 
			color: #aaa; 
			border: none;
			padding: 0.5em 0.4em 0.4em 0.5em;
			margin:  0.0em 0.1em 0.5em 0.1em;
			background-color: rgba(80, 80, 80, 50);
			border-bottom-right-radius: 3px;
			border-bottom-left-radius: 3px;
		}}

		QTabBar:tab::hover {{ 
			color: #ddd; 
			background-color: rgba(150, 150, 150, 50);
		}}

		QToolBar{{
			border: 1px solid rgba(50, 50, 50, 120);
			background-color: rgba(0,0,0, 255);
		}}

		QToolBar::handle {{ 
			image: url(:/icons/toolbar_handle.png); 
		}}

		QToolButton {{
			color : #aaa; 
			border: 1px solid rgba(50, 50, 50, 120);
			background-color :rgba(30, 30, 30, 120);
			padding: 0.3em 0.3em 0.3em 0.3em;
			margin:  0.3em 0.3em 0.3em 0.3em;
			border-radius: 3px;
		}}

		QToolButton::hover  {{
			color : #ddd; 
			background-color : rgba(150, 150, 150, 50);
		}}

	"""

def widget_theme(theme = None):
	theme = theme if theme else default_theme
	return f"""
		QWidget{{background-color :{theme['widget_bg_color']}; }}

	"""