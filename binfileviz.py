import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

class BinaryFileVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title("Binary File Visualizer")

        # Setting up the GUI
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.choose_file_button = tk.Button(self.frame, text="Choose File", command=self.load_file)
        self.choose_file_button.pack()

        self.canvas = tk.Canvas(self.master, bg="gray")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.save_binary_button = tk.Button(self.frame, text="Save Binary", command=self.save_binary)
        self.save_binary_button.pack(side=tk.LEFT)

        self.save_decimal_button = tk.Button(self.frame, text="Save Decimal", command=self.save_decimal)
        self.save_decimal_button.pack(side=tk.RIGHT)

        # Attributes for file processing
        self.binary_array = None
        self.image = None

    def load_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.process_file(file_path)

    def process_file(self, file_path):
        with open(file_path, 'rb') as file:
            data = file.read()
            self.binary_array = np.unpackbits(np.frombuffer(data, dtype=np.uint8))

            width = 256
            height = len(self.binary_array) // width
            if height * width < len(self.binary_array):
                height += 1

            self.image = Image.new("RGB", (width, height), "gray")
            pixels = self.image.load()

            for i in range(len(self.binary_array)):
                x = i % width
                y = i // width
                color = "black" if self.binary_array[i] == 1 else "white"
                pixels[x, y] = ImageColor.getrgb(color)

            self.display_image()

    def display_image(self):
        self.canvas_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.canvas_image)
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

    def save_binary(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".bin")
        if file_path:
            with open(file_path, 'wb') as file:
                np.packbits(self.binary_array).tofile(file)

    def save_decimal(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, 'w') as file:
                for byte in np.packbits(self.binary_array):
                    file.write(f"{byte}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = BinaryFileVisualizer(root)
    root.mainloop()
