import subprocess
import threading
import os
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

def install_dependencies():
    try:
        subprocess.run("pip install spotify_dl", shell=True, check=True)
        subprocess.run("pip install ffmpeg-python", shell=True, check=True)
        subprocess.run("pip install --upgrade sentry-sdk", shell=True, check=True)
        subprocess.run("pip install tk", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error durante la instalación: {e}")
        exit(1)

def set_spotify_env_vars():
    si = messagebox.askyesno("Spotify Client ID", "¿Tienes las Spotify Client ID?")
    if not si:
        ids = simpledialog.askstring("Spotify Client ID", "Pon aquí tu client id de Spotify: ")
        idp = simpledialog.askstring("Spotify Client ID", "Pon aquí tu Private client id de Spotify: ")
        os.environ['SPOTIPY_CLIENT_ID'] = ids
        os.environ['SPOTIPY_CLIENT_SECRET'] = idp
        messagebox.showinfo("Variables de entorno", "Variables de entorno establecidas. Por favor, reinicia el script para que los cambios tengan efecto.")
        exit(0)

def download_spotify(link, output_path):
    subprocess.run(f"spotify_dl -l {link} -o {output_path}", shell=True)

def on_download_click():
    link = link_entry.get()
    output_path = filedialog.askdirectory(title="Seleccionar Carpeta de Descarga")
    if output_path:
        download_thread = threading.Thread(target=download_spotify, args=(link, output_path))
        download_thread.start()
        messagebox.showinfo("Descarga iniciada", "La descarga ha comenzado. Se notificará cuando se complete.")

def cleanup():
    print("Limpiando...")
    exit(0)

root = tk.Tk()
root.title("Spotify Downloader")

root.geometry("400x300")
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text="Spotify Downloader", font=("Helvetica", 20), bg="#f0f0f0")
title_label.pack(pady=10)

install_btn = tk.Button(root, text="Instalar Dependencias", command=install_dependencies, bg="#4caf50", fg="white", font=("Helvetica", 12))
install_btn.pack(pady=5)

set_env_btn = tk.Button(root, text="Establecer Variables de Entorno", command=set_spotify_env_vars, bg="#2196f3", fg="white", font=("Helvetica", 12))
set_env_btn.pack(pady=5)

link_label = tk.Label(root, text="Pega tu playlist/canción de Spotify:", bg="#f0f0f0", font=("Helvetica", 12))
link_label.pack(pady=5)

link_entry = tk.Entry(root, width=40, font=("Helvetica", 12))
link_entry.pack(pady=5)

download_btn = tk.Button(root, text="Descargar", command=on_download_click, bg="#ff5722", fg="white", font=("Helvetica", 12))
download_btn.pack(pady=10)

root.protocol("WM_DELETE_WINDOW", cleanup)
root.mainloop()
