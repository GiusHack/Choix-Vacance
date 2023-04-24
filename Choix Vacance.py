import random
import tkinter as tk

destinations = ['Bali', 'Tokyo', 'Barcelone', 'New York',
                'Londres', 'Rio de Janeiro', 'Dubai', 'Sydney']


def choose_destination():
    destination = random.choice(destinations)
    result_label.configure(text=destination)


root = tk.Tk()
root.title("Choisissez votre prochaine destination de vacances")

instruction_label = tk.Label(
    root, text="Cliquez sur le bouton pour choisir votre prochaine destination de vacances !")
instruction_label.pack(pady=10)

choose_button = tk.Button(root, text="Choisir", command=choose_destination)
choose_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
