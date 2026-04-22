from fastapi import FastAPI
import sqlite3

def iniciar_db():
    conn = sqlite.connect("letterbox.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS peliculas (
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
    conn = sqlite3.connect("letterbox.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM peliculas")
    res = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return res

@app.post("/peliculas")
def cargar_una_pelicula(titulo, genero, puntaje):
    if not puntaje.isdigit():
        mensaje_de_retorno = "el puntaje tiene que ser un número entero"
        return mensaje_de_retorno
    conn = sqlite.connect("letterbox.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO peliculas (titulo, genero, puntaje)
    """)
    conn.commit()
    conn.close()
    mensaje_de_retorno = "Película guardada correctamente"
    return mensaje_de_retorno
