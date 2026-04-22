fastapi, uvicorn -> libraries python para APIs. fastapi es más básica...

uvicorn main:app --reload  -> Le pedimos a uvicorn que levante un servidor con la api "app".
            --reload es para que si lo corremos varias veces, apaga y prende la api.
En la página que genera (puede ser necesario entrar con Ctrl-click), se puede agregar /docs a la url para que muestre una interfaz con la descripción de la API.
