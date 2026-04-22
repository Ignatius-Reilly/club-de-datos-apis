from fastapi import FastAPI

db_peliculas = [{"titulo": "Matrix", "genero": "Accion", "puntaje": 5},
                {"titulo": "Esperando la Carroza", "genero": "Comedia", "puntaje": 5},
]

app = FastAPI()

@app.get("/peliculas")
def obtener_películas():
    return db_peliculas
