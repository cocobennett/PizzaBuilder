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
    size = tk.Label(tab, text="Size       ", font=("Arial Bold", 16))
    grid(size, 0, 0)
    size_option = create_size_options(tab)
    crust = tk.Label(tab, text="Crust      ", font=("Arial Bold", 16))
    grid(crust, 0, 2)
    crust_options = create_crust_options(tab)
    add_ons = tk.Label(tab, text="Add-Ons", font=("Arial Bold", 16))
    grid(add_ons, 0, 4)
    add_on_options = create_add_on_options(tab)
    button = tk.Button(tab, text="Next", command=clicked)
    grid(button, 0, 6)

def clicked():
    print("Button was clicked!")

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
    return selected

def create_crust_options(tab):
    selected = tk.IntVar()
    thin = tk.Radiobutton(tab, text='Thin', value=1, variable=selected, command=partial(get_value, selected))
    grid(thin, 0, 3)
    hand = tk.Radiobutton(tab, text='Hand Tossed', value=2, variable=selected, command=partial(get_value, selected))
    grid(hand, 1, 3)
    pan = tk.Radiobutton(tab, text='Pan', value=3, variable=selected, command=partial(get_value, selected))
    grid(pan, 2, 3)
    return selected

def create_add_on_options(tab):
    selected = tk.IntVar()
    none = tk.Radiobutton(tab, text='None', value=1, variable=selected, command=partial(get_value, selected))
    grid(none, 0, 5)
    stuffed = tk.Radiobutton(tab, text='Stuffed Crust', value=2, variable=selected, command=partial(get_value, selected))
    grid(stuffed, 1, 5)
    return selected

def get_value(selected):
    #print(selected.get())
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
