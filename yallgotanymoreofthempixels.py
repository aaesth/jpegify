import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def downscale_image(input_path, output_path, scale_factor=10):
    try:
        # Open an image file
        with Image.open(input_path) as img:
            # Calculate the new size
            new_size = (img.width // scale_factor, img.height // scale_factor)
            
            # Downscale the image
            downscaled_img = img.resize(new_size, Image.LANCZOS)
            
            # Save the downscaled image
            downscaled_img.save(output_path)
            messagebox.showinfo("it worked!!!!!", f"saved to {output_path}")
    except Exception as e:
        messagebox.showerror("error", f"failed to downscale image: {e}")

def select_image():
    # Open file dialog to select an image file
    input_path = filedialog.askopenfilename(
        filetypes=[("image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    
    if input_path:
        # Open file dialog to select where to save the downscaled image
        output_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"),
                       ("BMP files", "*.bmp"), ("GIF files", "*.gif")])
        
        if output_path:
            downscale_image(input_path, output_path)

# Create the main window
root = tk.Tk()
root.title("jpepgify")

# Create and place the button to select an image
btn_select_image = tk.Button(root, text="select image to ruin", command=select_image)
btn_select_image.pack(pady=20)

# Run the application
root.mainloop()
