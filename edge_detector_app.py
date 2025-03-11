import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

# Initialize Tkinter window
root = tk.Tk()
root.title("Edge Detector App")
root.geometry("600x500")

# Global variables
img = None
original_img = None
panel = None

def load_image():  
    global img, original_img, tk_img, panel
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg; *.png; *.jpeg")])
    if not file_path:
        return  

    img = cv2.imread(file_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    original_img = img.copy()  # Save original for reset

    # Convert to Tkinter-compatible format
    img_pil = Image.fromarray(img)
    tk_img = ImageTk.PhotoImage(img_pil)

    # Display image in Tkinter window
    if panel is None:
        panel = tk.Label(root, image=tk_img)
        panel.pack(pady=10)
    else:
        panel.config(image=tk_img)
        panel.image = tk_img

def reset_image():
    global img, tk_img
    if original_img is not None:
        img = original_img.copy()

        img_pil = Image.fromarray(img)
        tk_img = ImageTk.PhotoImage(img_pil)
        panel.config(image=tk_img)
        panel.image = tk_img

def apply_canny():
    global img, tk_img
    if img is None:
        return  

    # Convert to grayscale for edge detection
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    canny = cv2.Canny(gray, 150, 175)

    # Convert to Tkinter-compatible format
    canny_pil = Image.fromarray(canny)
    tk_img = ImageTk.PhotoImage(canny_pil)
    
    # Update panel
    panel.config(image=tk_img)
    panel.image = tk_img

    # Show in OpenCV window
    cv2.imshow('Canny Edge Detection', canny)

def apply_sobel():
    global img, tk_img
    if img is None:
        return  

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    sobel = cv2.Sobel(gray, cv2.CV_64F, 1, 1, ksize=5)
    sobel = cv2.convertScaleAbs(sobel)

    sobel_pil = Image.fromarray(sobel)
    tk_img = ImageTk.PhotoImage(sobel_pil)
    
    panel.config(image=tk_img)
    panel.image = tk_img

    cv2.imshow('Sobel Edge Detection', sobel)

def apply_laplacian():
    global img, tk_img
    if img is None:
        return  

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)

    laplacian_pil = Image.fromarray(laplacian)
    tk_img = ImageTk.PhotoImage(laplacian_pil)
    
    panel.config(image=tk_img)
    panel.image = tk_img

    cv2.imshow('Laplacian Edge Detection', laplacian)

def apply_gaussian_blur():
    global img, tk_img
    if img is None:
        return  

    blurred = cv2.GaussianBlur(img, (15, 15), 0)

    blurred_pil = Image.fromarray(blurred)
    tk_img = ImageTk.PhotoImage(blurred_pil)
    
    panel.config(image=tk_img)
    panel.image = tk_img

def apply_thresholding():
    global img, tk_img
    if img is None:
        return  

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, thresholded = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    threshold_pil = Image.fromarray(thresholded)
    tk_img = ImageTk.PhotoImage(threshold_pil)
    
    panel.config(image=tk_img)
    panel.image = tk_img

def save_image():
    if img is None:
        return  

    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"),
                                                        ("JPEG files", "*.jpg"),
                                                        ("All Files", "*.*")])
    if file_path:
        cv2.imwrite(file_path, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

def exit_app():
    root.quit()

# Layout using Frames
frame1 = tk.Frame(root)
frame1.pack(pady=10)

frame2 = tk.Frame(root)
frame2.pack(pady=5)

frame3 = tk.Frame(root)
frame3.pack(pady=5)

frame4 = tk.Frame(root)
frame4.pack(pady=5)

# Row 1: Image selection
btn_load = tk.Button(frame1, text="Load Image", command=load_image)
btn_load.pack(side=tk.LEFT, padx=5)

btn_reset = tk.Button(frame1, text="Reset Image", command=reset_image)
btn_reset.pack(side=tk.LEFT, padx=5)

# Row 2: Edge detection
btn_canny = tk.Button(frame2, text="Apply Canny", command=apply_canny)
btn_canny.pack(side=tk.LEFT, padx=5)

btn_sobel = tk.Button(frame2, text="Apply Sobel", command=apply_sobel)
btn_sobel.pack(side=tk.LEFT, padx=5)

btn_laplacian = tk.Button(frame2, text="Apply Laplacian", command=apply_laplacian)
btn_laplacian.pack(side=tk.LEFT, padx=5)

# Row 3: Preprocessing
btn_gaussian = tk.Button(frame3, text="Gaussian Blur", command=apply_gaussian_blur)
btn_gaussian.pack(side=tk.LEFT, padx=5)

btn_threshold = tk.Button(frame3, text="Thresholding", command=apply_thresholding)
btn_threshold.pack(side=tk.LEFT, padx=5)

# Row 4: Save & Exit
btn_save = tk.Button(frame4, text="Save Image", command=save_image)
btn_save.pack(side=tk.LEFT, padx=5)

btn_exit = tk.Button(frame4, text="Exit", command=exit_app)
btn_exit.pack(side=tk.LEFT, padx=5)

# Run the Tkinter main loop
root.mainloop()
