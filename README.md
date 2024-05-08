# react-scheduler-crud-django-mysql

Syncfusion [React Scheduler](https://ej2.syncfusion.com/react/demos/#/material3/schedule/overview) CRUD Application with Django and MySQL database.

# Pre-requisites

1. Python 3.6 or above
2. Django 3.0 or above
3. MySQL 5.7 or above
4. React 16.8 or above
5. Node 16.17 or above


# Steps to run the project
1. Clone the repository
2. Run the following command to install the required packages
    ```
    pip install django-cors-headers
    pip install djangorestframework
    pip install pymysql
    pip install dj-database-url
    pip install mysqlclient
    ```
3. Go to the backend directory 
4. Need to configure your database in the `backend/scheduler/settings.py` file
   ```
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Your database',
        'USER': 'Your username',
        'PASSWORD': 'Your password',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
    }
    ```
5. We need to create table in the mysql database. Run the following command to create the table

    ```
   python manage.py makemigrations

   python manage.py migrate

   ```
6. Now lets run the server

    ```
    python manage.py runserver
    ```
    you will the server is running at http://127.0.0.1:8000/

7. Now open another terminal, on the root directory, run the following command to install the required packages
    ```
    npm install
    ```
8. Run the following command to start the react server
    ```
    npm run start
    ```
    you will see the react server is running at http://localhost:3000/

9. Now you can see the scheduler application running in the browser, and you can able to perform crud operations in the scheduler.
