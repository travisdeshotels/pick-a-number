from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

def get_main_layout(*layouts):
    vertical_layout = QVBoxLayout()
    for layout in layouts:
        vertical_layout.addLayout(layout)

    return vertical_layout

def get_horizontal_layout_with_widgets_and_alignment(widgets, alignment=None):
    layout = QHBoxLayout()
    for widget in widgets:
        layout.addWidget(widget)
    if alignment is not None:
        layout.setAlignment(alignment)

    return layout
