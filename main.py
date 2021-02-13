import tkinter as tk
import tkinter.ttk as ttk

def main():
    w = create_window()
    tabs = create_tabs(w)
    crust_options(tabs["crust"])
    open_window(w)

def crust_options(tab):
    size = tk.Label(tab, text="Size", anchor="w", width="20", font=("Arial Bold", 16))
    grid(size, 0, 0)
    small = tk.Radiobutton(tab, text='Small', value=1)
    grid(small, 0, 1)
    med = tk.Radiobutton(tab, text='Mediuam', value=2)
    grid(med, 1, 1)
    large = tk.Radiobutton(tab, text='Large', value=3)
    grid(large, 2, 1)
    ex_large = tk.Radiobutton(tab, text='Extra Large', value=4)
    grid(ex_large, 3, 1)
    crust = tk.Label(tab, text="Crust", anchor="w", width="20", font=("Arial Bold", 16))
    grid(crust, 0, 2)
    add_ons = tk.Label(tab, text="Add-Ons", anchor="w", width="20", font=("Arial Bold", 16))
    grid(add_ons, 0, 4)

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
