from python_modules.gui_shop.canvas import tk


def clean_screen():
    for el in tk.grid_slaves():
        el.destroy()