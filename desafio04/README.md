sudo docker-compose run web django-admin startproject mysite .
sudo chown -R $USER:$USER .

sudo docker-compose run web python manage.py startapp maratona

sudo docker-compose run web python manage.py runserver