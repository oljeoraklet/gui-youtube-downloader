import tkinter as tk
import customtkinter as ctk
from pytube import YouTube

# System settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Frame
app = ctk.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Elements
title = ctk.CTkLabel(app, text="YouTube Downloader", font=("Arial", 20))
title.pack(padx=10, pady=10)

video_title = ctk.CTkLabel(app, text="", font=("Arial", 14))
video_title.pack(padx=10, pady=10)


# Input URL
url = tk.StringVar()
input_url = ctk.CTkEntry(app, width=300, font=("Arial", 12),  textvariable=url)
input_url.pack(padx=10, pady=10)

# Download button
def download():
    try:
        youtube_url = url.get()
        yt = YouTube(youtube_url, on_progress_callback=download_percentage_calc)
        
        video_title.configure(text=yt.title)
        video = yt.streams.get_highest_resolution()
        thumbnail = yt.thumbnail_url
        # print(thumbnail)
        video.download()
        finished_label.configure(text="Downloaded successfully")
        print("Downloaded successfully")
    except:
        finished_label.configure(text="Something went wrong. Please try again", text_color="red")
    

def download_percentage_calc(stream, chunk, bytes_remaining):
    download_progress.pack()
    percentage_label.pack(padx=10, pady=10)

    size = stream.filesize
    bytes_downloaded = size - bytes_remaining
    percentage = bytes_downloaded / size * 100
    percentage_label.configure(text=str(int(percentage)) + "%")
    print(percentage)
    print(float(percentage) / 100)
    download_progress.set(float(percentage) / 100)
    if(percentage == 100.0):
        download_progress.pack_forget()
    app.update()

    

download_button = ctk.CTkButton(app, text="Download", font=("Arial", 12), command=download)
download_button.pack(padx=10, pady=10)

download_progress = ctk.CTkProgressBar(app, width=300)
download_progress.set(0)

percentage_label = ctk.CTkLabel(app, text="", font=("Arial", 12))

finished_label = ctk.CTkLabel(app, text="0%", font=("Arial", 12))
finished_label.pack(padx=10, pady=10)


check_var = tk.StringVar()
def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())

checkbox = ctk.CTkCheckBox(master=app, text="CTkCheckBox", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")
checkbox.pack(padx=20, pady=10)

# Main function
app.mainloop()