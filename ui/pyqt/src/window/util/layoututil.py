from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

def get_main_layout(horizontal_layout1, horizontal_layout2, horizontal_layout3, horizontal_layout4, horizontal_layout5, horizontal_layout6, horizontal_layout7):
    vertical_layout = QVBoxLayout()
    vertical_layout.addLayout(horizontal_layout1)
    vertical_layout.addLayout(horizontal_layout2)
    vertical_layout.addLayout(horizontal_layout3)
    vertical_layout.addLayout(horizontal_layout4)
    vertical_layout.addLayout(horizontal_layout5)
    vertical_layout.addLayout(horizontal_layout6)
    vertical_layout.addLayout(horizontal_layout7)

    return vertical_layout

def get_main_layout_for_config_window_no_secret(horizontal_layout1, horizontal_layout2, horizontal_layout3, horizontal_layout4, horizontal_layout5, horizontal_layout6):
    vertical_layout = QVBoxLayout()
    vertical_layout.addLayout(horizontal_layout1)
    vertical_layout.addLayout(horizontal_layout2)
    vertical_layout.addLayout(horizontal_layout3)
    vertical_layout.addLayout(horizontal_layout4)
    vertical_layout.addLayout(horizontal_layout5)
    vertical_layout.addLayout(horizontal_layout6)

    return vertical_layout

def get_main_layout_for_config_window_with_secret(horizontal_layout1, horizontal_layout2, horizontal_layout3, horizontal_layout4, horizontal_layout5):
    vertical_layout = QVBoxLayout()
    vertical_layout.addLayout(horizontal_layout1)
    vertical_layout.addLayout(horizontal_layout2)
    vertical_layout.addLayout(horizontal_layout3)
    vertical_layout.addLayout(horizontal_layout4)
    vertical_layout.addLayout(horizontal_layout5)

    return vertical_layout

def get_horizontal_layout_with_widgets_and_alignment(widgets, alignment=None):
    layout = QHBoxLayout()
    for widget in widgets:
        layout.addWidget(widget)
    if alignment is not None:
        layout.setAlignment(alignment)

    return layout
