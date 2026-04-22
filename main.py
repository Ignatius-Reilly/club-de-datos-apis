from fastapi import FastAPI
import sqlite3

def iniciar_db():
    conn = sqlite.connect("letterbox.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXIST peliculas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        genero TEXT,
        puntaje INTEGER)
    """)
    conn.commit()
    conn.close()

generos = []

app = FastAPI()

@app.get("/peliculas")
def obtener_películas():
    return db_peliculas

@app.post("/peliculas")
def cargar_una_pelicula(titulo, genero, puntaje):
    if not puntaje.isdigit():
        mensaje_de_retorno = "el puntaje tiene que ser un número entero"
        return mensaje_de_retorno
    if not genero in generos:
        mensaje_de_retorno = "El género indicado no es válido"
        return mensaje_de_retorno
    nueva_pelicula = {"titulo": titulo, "genero": genero, "puntaje": puntaje}
    db_peliculas.append(nueva_pelicula)
    mensaje_de_retorno = "Película guardada correctamente"
    return mensaje_de_retorno

@app.get("/genero")
def obtener_genero():
    return generos

@app.post("/genero")
def añadir_genero(genero):
    generos.append(genero)
    mensaje_de_retorno = "Género añadido correctamente."
    return mensaje_de_retorno
