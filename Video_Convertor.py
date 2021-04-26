"""
    Python program to implement video convertor
"""
from random import choices
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube  # pip install pytube3

folder_name = ""

# file location
def open_file():
    global folder_name
    folder_name = filedialog.askdirectory()
    if len(folder_name) > 1:  # If file is selected.......it means select location instead of null value
        location_error.config(text=folder_name, fg="blue")
    else:
        location_error.config(text="Please select the location!", fg="blue")


# Download video
def download_video():
    choice = ytd_choices.get()  # It will fetch user choice
    url = ytd_entry.get()  # It will get url from ytd_entry box

    if len(url) > 1:
        ytd_error.config(text="")
        yt = YouTube(url)

        if choice == choices[0]:
            select = yt.streams.filter(progressive=True).first()

        elif choice == choices[1]:
            select = yt.streams.filter(progressive=True, file_extension="mp3").last()

        elif choice == choices[2]:
            select = yt.streams.filter(progressive=True).first()

        elif choice == choices[3]:
            select = yt.streams.filter(progressive=True).first()

        elif choice == choices[4]:
            select = yt.streams.filter(progressive=True).first()

        elif choice == choices[5]:
            select = yt.streams.filter(progressive=True).first()

        else:
            ytd_error.config(text="Paste a link again!", fg="blue")

    # Download function
    select.download(folder_name)
    ytd_error.config(text="Download complete")


root = Tk()
root.title("Video Convertor")
root.geometry("350x400")  # set window
root.columnconfigure(0, weight=1)  # set all contents in center

# Label
ytd_label = Label(root, text="Enter a URL of video", font=("helvetica", 15))
ytd_label.grid()

# Entry box to paste url
ytd_entry_var = StringVar()
ytd_entry = Entry(root, width=40, font=("helvetica", 16), textvariable=ytd_entry_var)
ytd_entry.grid()

# Error message
ytd_error = Label(root, text="Please enter a valid URL", font=("helvetica", 10), fg="red")
ytd_error.grid()

# Ask to save file location
save_label = Label(root, text="Save the video file", font=("helvetica", 15, "bold"))
save_label.grid()

# Sava button
save_entry = Button(root, text="Location", width=10, fg="white", bg="green", command=open_file)
save_entry.grid()

# Location error
location_error = Label(root, text="Please select the location", fg="red", font=("helvetica", 10))
location_error.grid()

# Download quality
ytd_quality = Label(root, text="Select quality", font=("helvetica", 15))
ytd_quality.grid()

# combobox for quality options
choice = ["1080", "720", "360", "144", "MP3"]
ytd_choices = ttk.Combobox(root, values=choice)
ytd_choices.grid()

# Download button
download = Button(root, text='Download', font="helvetica", fg="white", bg="green", width=15, command=download_video)
download.grid()

root.mainloop()
