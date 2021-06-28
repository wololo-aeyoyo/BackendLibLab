# BackendLibLab
## Backend de la prueba de liblab

1- clonar la aplicacion

    git clone https://github.com/wololo-aeyoyo/BackendLibLab.git

2- cd a la carpeta

    cd BackendLibLab

3- instalar el ambiente virtual de python

    pip install virtualenv

4- crear el ambiente virtual de python

    virtualenv amb

5-activar el ambiente en windows

    .\amb\Scripts\activate

6-Instalar el requiriments.txt

    pip install -r requiriments.txt

7-Debemos crear la base de datos  desde el pgadmin4 con nombre `creditoSBS` y configurar el `settings.py` con la informacion de la instancia de postgresql

    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'creditoSBS',
          'USER': 'postgres',
          'PASSWORD':'pass',
          'HOST':'localhost',
          'PORT':'5432'
      }
     }



8-hacer las migraciones

    python manage.py makemigrations
    python manage.py migrate
    
9-Correr el servidor

    python manage.py runserver

***
## El servidor emepezara a correr en 

`http://127.0.0.1:8000/`

Creamos un super usuario

    python manage.py createsuperuser

Procedemos a poblar las tablas de **usuarios** `(minimo con 2 usuarios)` y la tabla de **puntuacion** en el orden señalado en la imagen
***
Nos logeamos en `http://localhost:8000/admin`

![Test Image 1](https://i.imgur.com/ggV9IQR.png)

Alli editaremos dos tablas `Puntuacionss` y `Usuarioss`

![Test Image 2](https://i.imgur.com/iyKKbY3.png)

En `Usuarioss` añadimos como minimo 2 con sus correos, nombres y apellidos

![Test Image 3](https://i.imgur.com/U0rMGJ7.png)

En `Puntuacionss` añadimos clas puntuaciones de `malo` , `regular` y `bueno` en ese orden

![Test Image 4](https://i.imgur.com/3n2AyQr.png)
***

**Recuerda correr el Frontend** con `ng serve`

Deberias ver algo asi

![Test Image 5](https://i.imgur.com/uK0ehkz.png)
