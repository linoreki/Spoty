import subprocess
import threading
import os
import atexit


si = input("¿Tienes las Spotify Client ID? (S/N): ")

if si.upper() == "N":
    ids = input("Pon aquí tu client id de Spotify: ")
    idp = input("Pon aquí tu Private client id de Spotify: ")
    os.environ['SPOTIPY_CLIENT_ID'] = ids
    os.environ['SPOTIPY_CLIENT_SECRET'] = idp
    print("Variables de entorno establecidas. Por favor, reinicia el script para que los cambios tengan efecto.")
    exit(0)
elif si.upper() == "S":
    print("En caso de error, compruébalas.")



def download_spotify(link):
    subprocess.run(f"spotify_dl -l {link}", shell=True)

link = input("Pega tu playlist/canción de Spotify: ")

download_thread = threading.Thread(target=download_spotify, args=(link,))
download_thread.start()



download_thread.join()  

print("Cuando termine, encontrarás tus archivos en /users/name/Nombre de la playlist")

def cleanup():
    print("limpiando...")

atexit.register(cleanup)
