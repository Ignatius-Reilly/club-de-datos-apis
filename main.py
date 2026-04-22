from fastapi import FastAPI

db_peliculas = [{"titulo": "Matrix", "genero": "Accion", "puntaje": 5},
                {"titulo": "Esperando la Carroza", "genero": "Comedia", "puntaje": 5},
]

app = FastAPI()

@app.get("/peliculas")
def obtener_películas():
    return db_peliculas

@app.post("/peliculas")
def cargar_una_pelicula(titulo, genero, puntaje):
    nueva_pelicula = {"titulo": titulo, "genero": genero, "puntaje": puntaje}
    db_peliculas.append(nueva_pelicula)
    mensaje_de_retorno = "Película guardada correctamente"
    return mensaje_de_retorno
