To Do list
============

### Running the app on local computer

Start the Cloud SQL Proxy

```
./cloud_sql_proxy -instances="[INSTANCE_CONNECTION_NAME]"=tcp:3306
```

Create an isolated Python environment, and install dependencies
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
Start a local web server
```
python manage.py runserver
```

Deployed on https://todo-app-308514.ey.r.appspot.com/


