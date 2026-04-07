import requests
import tkinter as tk
from tkinter import Label, Entry, Button
from PIL import Image, ImageTk
import io
import pyttsx3  
API_KEY = "b606b089"  #my api key.
engine = pyttsx3.init()
engine.setProperty('rate', 150) 

def search_movie():
    movie_name = entry.get()
    if not movie_name:
        result_label.config(text="Please enter a movie name!", fg="red")
        return

    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={API_KEY}"
    print(f"Requesting: {url}")  # Log the URL to make sure it's correct
    
    # Make the API request
    response = requests.get(url).json()
    print(f"API Response: {response}")  # Log the full response

    if response["Response"] == "False":
        result_label.config(text=f"Movie '{movie_name}' not found! Try another.", fg="red")
        return

    # Get movie details from API response
    title = response.get("Title", "N/A")
    year = response.get("Year", "N/A")
    genre = response.get("Genre", "N/A")
    plot = response.get("Plot", "No plot available.")
    poster_url = response.get("Poster", None)

    # Update label text with movie details
    result_label.config(text=f"{title} ({year})\nGenre: {genre}\n\n{plot}", fg="black")

    # Speak the description using pyttsx3
    engine.say(f"{title}, released in {year}. Genre: {genre}. {plot}")
    engine.runAndWait()

    # Load and display movie poster
    if poster_url and poster_url != "N/A":
        load_poster(poster_url)
    else:
        poster_label.config(text="No Image Available", fg="red")

def load_poster(url):
    try:
        img_response = requests.get(url)
        img_data = img_response.content
        img = Image.open(io.BytesIO(img_data))
        img = img.resize((200, 300))
        img = ImageTk.PhotoImage(img)
        poster_label.config(image=img)
        poster_label.image = img
    except Exception as e:
        poster_label.config(text="No Image Available", fg="red")

# GUI Setup
root = tk.Tk()
root.title("Movie Finder 🎬")
root.geometry("500x650")
root.configure(bg="white")

# Search bar
entry = Entry(root, font=("Arial", 16), width=30)
entry.pack(pady=20)

# Search button
search_button = Button(root, text="🔍 Search", font=("Arial", 14), command=search_movie)
search_button.pack(pady=5)

# Result label
result_label = Label(root, text="Enter a movie name and press search!", font=("Arial", 12), wraplength=450, bg="white")
result_label.pack(pady=20)

# Poster image label
poster_label = Label(root, bg="white")
poster_label.pack()

# Run the application
root.mainloop()
