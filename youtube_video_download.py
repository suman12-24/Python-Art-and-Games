import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp

def download_youtube_video(url, save_path):
    ydl_opts = {
        'outtmpl': save_path + '/%(title)s.%(ext)s',  # Save the video with its title as the filename
        'format': 'best',  # Download the best available quality
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo('Success', 'Download completed.')
    except Exception as e:
        messagebox.showerror('Error', f'Error: {e}')

def start_download():
    url = url_entry.get()
    if not url:
        messagebox.showwarning('Input Error', 'Please enter a YouTube URL.')
        return
    save_path = filedialog.askdirectory()
    if not save_path:
        messagebox.showwarning('Input Error', 'Please select a save directory.')
        return
    download_youtube_video(url, save_path)

# Set up the GUI
root = tk.Tk()
root.title('YouTube Video Downloader')

tk.Label(root, text='YouTube URL:').pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(root, text='Download', command=start_download)
download_button.pack(pady=20)

root.mainloop()
