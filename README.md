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

    python manage.py migrate
***
## El servidor emepezara a correr en 

`http://127.0.0.1:8000/`

**Recuerda correr el Frontend** con `ng serve`

