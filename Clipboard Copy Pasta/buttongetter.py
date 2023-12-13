import tkinter as tk

def obtainWord(input, dict, output):
    text = input.get(1.0, "end-1c")
    dict.append(text)
    output.insert(tk.END, dict)