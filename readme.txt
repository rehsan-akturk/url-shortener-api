1.Create you virtualenv and install the packages
    pip install -r requirements.txt

2.Initialize database and create the database mapping used for persistance in the url shortener API.

   python manage.py makemigrations


3.Apply the database mapping from the app to the database; migrate the database.

  python manage.py migrate

4.Run the application.
   python manage.py runserver
   
   
   
 
 
 Test:
 
 GET=http://localhost:8000
 
 post=http://localhost:8000
 
 example post:
 
 {
   "url":"https://github.com/"
 
 }