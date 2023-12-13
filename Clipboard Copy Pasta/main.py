import tkinter as tk
import buttongetter

dict = ["hello"] #stores input keyword

root = tk.Tk()
root.title("Copy Pasta App")
root.geometry('480x720')

input = tk.Text(root, height = 1, width = 40)
input.pack()
dict_display = tk.Text(root, height = 3, width = 40)
button_copy = tk.Button(root, text = "add to dictionary", command = buttongetter.obtainWord(input, dict, dict_display))
button_copy.pack()


dict_display.pack()

# button_tracker = tk.Button(root, text = "display dictionary", command = buttongetter.displayText(dict, dict_display))
# button_tracker.pack()

root.mainloop()