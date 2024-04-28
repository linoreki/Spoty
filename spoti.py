import subprocess
import threading
import os
import atexit

try:
    subprocess.run("pip install spotify_dl", shell=True, check=True)
    subprocess.run("pip install ffmpeg-python", shell=True, check=True)
    subprocess.run("pip install --upgrade sentry-sdk", shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error durante la instalación: {e}")
    exit(1)

si = input("Tienes las Spotify Client ID? (S/N): ")

if si.upper() == "N":
    ids = input("Pon aqui tu client id de Spotify: ")
    idp = input("Pon aquí tu Private client id de Spotify: ")
    os.environ['SPOTIPY_CLIENT_ID'] = ids
    os.environ['SPOTIPY_CLIENT_SECRET'] = idp
    print("Variables de entorno establecidas. Por favor, reinicia el script para que los cambios tengan efecto.")
    exit(0)
elif si.upper() == "S":
    print("En caso de error, comprurbalas.")

print("Recuerda que debes tener instalado Python en el ordenador.")


def download_spotify(link):
    subprocess.run(f"spotify_dl -l {link}", shell=True)

link = input("Pega tu playlist/cancion de Spotify: ")

download_thread = threading.Thread(target=download_spotify, args=(link,))
download_thread.start()



download_thread.join()  

print("Cuando termine, encontrarás tus archivos en /users/name/Nombre de la playlist")

def cleanup():
    print("limpiando...")

atexit.register(cleanup)
