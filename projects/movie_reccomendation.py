import tkinter as tk
from PIL import Image, ImageTk
import random
import os
from io import BytesIO
import requests

poster_folder = "movie_posters\\poster_folder"
movie_images = {}
for file in os.listdir(poster_folder):
    if file.lower().endswith((".jpg", ".png", ".jpeg")):
        movie_name = os.path.splitext(file)[0]  # filename without extension
        movie_images[movie_name] = os.path.join(poster_folder, file)
movie_images["Avengers"] = "movie_posters\\poster_folder\\avengers.jfif"

# Movie list
movie_list = list(movie_images.keys())
def recommend_movie():
    movie = random.choice(movie_list)
    result_label.config(text=f"🎬 You should watch: {movie}")

    img_path = movie_images.get(movie)
    try:
        if img_path.startswith("http"):  # online image
            import requests
            from io import BytesIO
            response = requests.get(img_path)
            img = Image.open(BytesIO(response.content))
        else:  # local image
            img = Image.open(img_path)

        img = img.resize((150, 200))
        img_tk = ImageTk.PhotoImage(img)
        poster_label.config(image=img_tk, text="")
        poster_label.image = img_tk  # keep reference
    except Exception as e:
        poster_label.config(text="Image not found!", image="")
        print("Error loading image:", e)

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Movie Recommendation System")
root.geometry("400x450")
root.configure(bg="#f0f0f0")


heading = tk.Label(root, text="🎬 Movie Recommendation System", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
heading.pack(pady=10)
recommend_btn = tk.Button(root, text="Recommend a Movie", command=recommend_movie, font=("Helvetica", 12), bg="#4CAF50", fg="white")
recommend_btn.pack(pady=10)
result_label = tk.Label(root, text="", font=("Helvetica", 12), fg="blue", bg="#f0f0f0")
result_label.pack(pady=10)
poster_label = tk.Label(root, bg="#f0f0f0")
poster_label.pack(pady=10)
exit_btn = tk.Button(root, text="Exit", command=exit_app, font=("Helvetica", 12), bg="#f44336", fg="white")
exit_btn.pack(pady=10)
root.mainloop()
