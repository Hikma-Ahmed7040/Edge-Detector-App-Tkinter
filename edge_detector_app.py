import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

# --- Initialize the main window ---
root = tk.Tk()
root.title("Edge Detector App")
root.geometry("600x500")  # Size of the main window

# --- Global variables ---
img = None               # Displayed image (can be transformed)
original_img = None      # Backup of original image for reset
panel = None             # Label widget to show image

# --- Resize image if it's too large for display ---
def resize_for_display(image, max_width=500, max_height=400):
    h, w = image.shape[:2]
    if w > max_width or h > max_height:
        scale_w = max_width / w
        scale_h = max_height / h
        scale = min(scale_w, scale_h)
        new_w, new_h = int(w * scale), int(h * scale)
        return cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)
    return image

# --- Load and display image ---
def load_image():  
    global img, original_img, tk_img, panel
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg; *.png; *.jpeg")])
    if not file_path:
        return  

    img = cv2.imread(file_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    img = resize_for_display(img)        # Resize for display window
    original_img = img.copy()            # Keep a copy of the original

    img_pil = Image.fromarray(img)       # Convert to PIL format
    tk_img = ImageTk.PhotoImage(img_pil) # Convert to Tkinter-compatible image

    if panel is None:
        panel = tk.Label(root, image=tk_img)
        panel.pack(pady=10)
    else:
        panel.config(image=tk_img)
        panel.image = tk_img

# --- Reset to original image ---
def reset_image():
    global img, tk_img
    if original_img is not None:
        img = original_img.copy()
        img_pil = Image.fromarray(img)
        tk_img = ImageTk.PhotoImage(img_pil)
        panel.config(image=tk_img)
        panel.image = tk_img

# --- Apply Canny Edge Detection ---
def apply_canny():
    global img, tk_img
    if img is None:
        return  
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    canny = cv2.Canny(gray, 150, 175)
    canny_pil = Image.fromarray(canny)
    tk_img = ImageTk.PhotoImage(canny_pil)
    panel.config(image=tk_img)
    panel.image = tk_img
    cv2.imshow('Canny Edge Detection', canny)

# --- Apply Sobel Edge Detection ---
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

# --- Apply Laplacian Edge Detection ---
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

# --- Apply Gaussian Blur for smoothing ---
def apply_gaussian_blur():
    global img, tk_img
    if img is None:
        return  
    blurred = cv2.GaussianBlur(img, (15, 15), 0)
    blurred_pil = Image.fromarray(blurred)
    tk_img = ImageTk.PhotoImage(blurred_pil)
    panel.config(image=tk_img)
    panel.image = tk_img

# --- Apply Simple Thresholding (Binary) ---
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

# --- Save current image ---
def save_image():
    if img is None:
        return  
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"),
                                                        ("JPEG files", "*.jpg"),
                                                        ("All Files", "*.*")])
    if file_path:
        cv2.imwrite(file_path, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

# --- Exit the application ---
def exit_app():
    root.quit()

# ------------------------ UI Layout ------------------------
frame1 = tk.Frame(root)
frame1.pack(pady=10)

frame2 = tk.Frame(root)
frame2.pack(pady=5)

frame3 = tk.Frame(root)
frame3.pack(pady=5)

frame4 = tk.Frame(root)
frame4.pack(pady=5)

# Row 1: Load/Reset
tk.Button(frame1, text="Load Image", command=load_image).pack(side=tk.LEFT, padx=5)
tk.Button(frame1, text="Reset Image", command=reset_image).pack(side=tk.LEFT, padx=5)

# Row 2: Edge detection methods
tk.Button(frame2, text="Apply Canny", command=apply_canny).pack(side=tk.LEFT, padx=5)
tk.Button(frame2, text="Apply Sobel", command=apply_sobel).pack(side=tk.LEFT, padx=5)
tk.Button(frame2, text="Apply Laplacian", command=apply_laplacian).pack(side=tk.LEFT, padx=5)

# Row 3: Preprocessing
tk.Button(frame3, text="Gaussian Blur", command=apply_gaussian_blur).pack(side=tk.LEFT, padx=5)
tk.Button(frame3, text="Thresholding", command=apply_thresholding).pack(side=tk.LEFT, padx=5)

# Row 4: Save and Exit
tk.Button(frame4, text="Save Image", command=save_image).pack(side=tk.LEFT, padx=5)
tk.Button(frame4, text="Exit", command=exit_app).pack(side=tk.LEFT, padx=5)

# --- Run the app ---
root.mainloop()
