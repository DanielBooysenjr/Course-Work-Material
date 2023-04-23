from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk
from tkinter import filedialog as fd

IMAGE_SIZE = (200, 200)

class WatermarkCreationTool():

    def __init__(self):
        self.window = Tk()
        self.window.geometry("600x400")
        self.window.title("Watermark Creation Tool")
        self.gui()
        self.window.mainloop()

    def open_image(self):
        self.filetypes = (
            ('text files', '*.txt'),
            ("all files", '*.*')
        )
        self.file = fd.askopenfilename(
            title="Select Image",
            initialdir='/',
            filetypes=self.filetypes
        )
        self.display_image = Canvas(
            self.window,
            width=300,
            height=300,
            )
        
        self.display_image.place(x=200, y=100)
        self.image = Image.open(self.file)
        self.resized = self.image.resize(IMAGE_SIZE)
        self.photo_image = ImageTk.PhotoImage(self.resized)
        self.display_image.create_image(0, 0, anchor=NW, image=self.photo_image)
        self.open_button.lift()
        self.add_watermark_b.lift()
        return self.file

    def add_watermark(self):
        text = self.text.get(1.0, END)
        name = self.new_file_name.get(1.0, END).strip()
        with Image.open(self.file).convert("RGBA") as base:
            watermarked_image = ImageDraw.Draw(base)
            font = ImageFont.truetype('arial.ttf', size=200)
            watermarked_image.text((100, 100), text, font=font ,fill=(211, 211, 211, 51))
            base.save(f"{name}.png")
            self.add_watermark_window.destroy()


    def add_watermark_button(self):
        self.add_watermark_window = Toplevel(self.window)
        self.add_watermark_window.geometry("500x300")
        self.add_watermark_window.title('Add Watermark')
        self.text = Text(
            self.add_watermark_window,
            height=2,
            width=50
            )
        self.steps = Label(
                        self.add_watermark_window,
                        text='Provide text of watermark'
                        )
        self.submit = Button(
            self.add_watermark_window,
            text='Submit',
            command=self.add_watermark
        )
        self.new_name = Label(
            self.add_watermark_window,
            text='New Name'
        )
        self.new_file_name = Text(
            self.add_watermark_window,
            height=1,
            width=20
        )

        self.submit.place(x=220, y=220)
        self.new_name.place(x=80, y=150)
        self.new_file_name.place(x=80, y=180)
        self.steps.place(x=50, y=20)
        self.text.place(x=50, y=70)
        return self.text

    
    def gui(self):
        intro = Label(text='Welcome to the watermark creation tool. Please select an image')
        self.open_button = Button(
            self.window,
            text='Choose Image',
            command=self.open_image,
               )
        
        self.add_watermark_b = Button(
            self.window,
            text='Add Watermark',
            command=self.add_watermark_button
        )

        intro.place(x=140, y=50)
        self.open_button.place(x=200, y=330)
        self.add_watermark_b.place(x=300, y=330)
        



WatermarkCreationTool()

