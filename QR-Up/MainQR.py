import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import ImageTk
import PIL
from pyzbar.pyzbar import decode
from PIL import Image as PILImage
import io
import time


root = tk.Tk()
root.title("QR-Up: A Code Generator and Decoder by Abhiraj Ghose")
root.geometry("600x600")


custom_font = ("Georgia", 12)



def generate_qr():
    input_text = input_entry.get()
    if input_text:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(input_text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")


        timestamp = time.strftime("%Y%m%d_%H%M%S")
        file_name = f"generated_qr_code_{timestamp}.png"

        file_path = f"C:\\Users\\shrey\\OneDrive\\Desktop\\Abhiraj_Ghose_Projects\\Python_Programs\\MyQR\\SavedQRCodes\\{file_name}"
        img.save(file_path)

        qr_image = PILImage.open(file_path)

        photo_image = PIL.ImageTk.PhotoImage(qr_image)

        qr_label.config(image=photo_image)
        qr_label.image = photo_image  
    else:
        messagebox.showwarning("Input Error", "Please enter some text or link to generate a QR code.")

def decode_qr():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if file_path:
        img = PILImage.open(file_path)
        decoded_objects = decode(img)
        if decoded_objects:
            decoded_text = decoded_objects[0].data.decode("utf-8")
            decoded_text_label.config(text=f"Decoded text: {decoded_text}")
        else:
            decoded_text_label.config(text="No QR code found.")
    else:
        messagebox.showwarning("File Error", "Please select a valid image file.")


name_label_1 = tk.Label(root, text="Welcome to QR-Up!", font=custom_font)
name_label_1.pack()
name_label_2 = tk.Label(root, text="Made By: ABHIRAJ GHOSE", font=custom_font)
name_label_2.pack()


space_label_1 = tk.Label(root)
space_label_1.pack()

generate_label = tk.Label(root, text="1. Generate QR Code from input link/text:", font=custom_font)
generate_label.pack()

input_label = tk.Label(root, text="Enter link/text:", font=custom_font)
input_label.pack()
input_entry = tk.Entry(root, width=45, font=custom_font)
input_entry.pack()

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr, font=(custom_font[0], custom_font[1], "bold"))
generate_button.pack()

qr_label = tk.Label(root)
qr_label.pack()



decode_label = tk.Label(root, text="2. Decode QR Code and display link/text:", font=custom_font)
decode_label.pack()

decode_button = tk.Button(root, text="Decode QR Code", command=decode_qr, font=(custom_font[0], custom_font[1], "bold"))
decode_button.pack()

space_label_2 = tk.Label(root)
space_label_2.pack()

decoded_text_label = tk.Label(root, text="", font=custom_font)
decoded_text_label.pack()

root.mainloop()
