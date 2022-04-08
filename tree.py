import tkinter as tk
from tkinter import ttk

def main():
    #Storing name of trees and their values
    trees = {'Tree1': 1.415, 'Tree2': 1.424, 'Tree3': 1.431, 'Tree4': 1.44, 'Tree5': 1.415, 'Tree6': 1.442}

    root = tk.Tk()

    root.title("Calculate Emission")

    root.configure(bg='Dodgerblue4')

    tk.Label(root, text='Choose Tree', bd=3).grid(row=0, column=0)

    trees_value = tk.StringVar()

    #Linking Trees keys and its values on GUI
    combo_material = ttk.Combobox(root, values=list(trees.keys()), justify="center", textvariable=trees_value)

    combo_material.bind('<<ComboboxSelected>>', lambda event: label_selected.config(text=trees[trees_value.get()]))
    combo_material.grid(row=0, column=1)

    combo_material.current(0)

    label_selected = tk.Label(root, text="Not Selected")

    label_selected.grid(row=2, column=1)
    
    number_0f_trees = tk.Text(root)
    number_0f_trees.grid(row=1, column=1)

    def clickme():
        try:
            emission = trees[trees_value.get()]
            num_trees = int(number_0f_trees.get('1.0', 'end'))

            label_selected = tk.Label(root, text=emission*num_trees)
            label_selected.grid(row=3, column=1)
        except ValueError:
            error = tk.Label(root, text="Please type number of trees in the above box. It should not be empty or a text")
            error.grid(row=3, column=1)

    button = ttk.Button(root, text="Calculate", command=clickme)
    button.grid(row=4, column=1)

    root.mainloop()

if __name__ == '__main__':
    main()