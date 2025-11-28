from pathlib import Path
import db
import graphql
import api


path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
    "db": db,
    "api": api,
    "graphql": graphql
}

def load(p):
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except:
        print("Paquete sin funcion init :c")

list(map(load, paths))
