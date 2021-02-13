import tkinter as tk
import tkinter.ttk as ttk
from pizza_class import Pizza
from functools import partial

pizza = Pizza()

def main():
    w = create_window()
    tabs = create_tabs(w)
    crust_options(tabs["crust"])
    open_window(w)

def crust_options(tab):
    size = tk.Label(tab, text="Size", font=("Arial Bold", 16))
    grid(size, 0, 0)
    size_option = create_size_options(tab)
    crust = tk.Label(tab, text="Crust", font=("Arial Bold", 16))
    grid(crust, 0, 2)
    add_ons = tk.Label(tab, text="Add-Ons", font=("Arial Bold", 16))
    grid(add_ons, 0, 4)

def create_size_options(tab):
    selected = tk.IntVar()
    small = tk.Radiobutton(tab, text='Small', value=1, variable=selected, command=partial(get_value, selected))
    grid(small, 0, 1)
    med = tk.Radiobutton(tab, text='Medium', value=2, variable=selected, command=partial(get_value, selected))
    grid(med, 1, 1)
    large = tk.Radiobutton(tab, text='Large', value=3, variable=selected, command=partial(get_value, selected))
    grid(large, 2, 1)
    ex_large = tk.Radiobutton(tab, text='Extra Large', value=4, variable=selected, command=partial(get_value, selected))
    grid(ex_large, 3, 1)
    return get_value(selected)

def get_value(selected):
    return selected.get()

def create_window():
    window = tk.Tk()
    window.title("Pizza Builder")
    window.geometry('500x300')
    return window

def create_tabs(window):
    control = ttk.Notebook(window)
    tabs = {}
    tabs["crust"] = create_tab(control, "Crust")
    tabs["sauce"] = create_tab(control, "Sauce")
    tabs["protein"] = create_tab(control, "Protein")
    tabs["toppings"] = create_tab(control, "Toppings")
    tabs["order"] = create_tab(control, "Order")
    control.pack(expand=1, fill="both")
    return tabs

def create_tab(control, title):
    tab = ttk.Frame(control)
    control.add(tab, text=title)
    return tab

def create_menu(window):
    menu = tk.Menu(window)
    menu.add_command(label="File")
    window.config(menu=menu)

def grid(panel, col, row):
    panel.grid(column=col, row=row)

def open_window(window):
    window.mainloop()

if __name__ == "__main__":
    main()
