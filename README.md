# Template-dj-cel-red-beat
This is a template project for Django-Celery-Redis-CeleryBeat

## Run Locally

Clone the project
```bash
  git clone https://github.com/akshay98322/template-dj-cel-red-beat.git
```

Go to the project directory
```bash
  cd template-dj-cel-red-beat
```

Install dependencies
```bash
  pip install -r requirements.txt
```

Start the server
```bash
  python manage.py runserver
```

Create Tables
```bash
  python manage.py migrate
```

Download and run docker desktop in your pc.

Start the redis service in a new terminal
```bash
  docker run -p 6379:6379 --name redis redis
```

Start the Celery worker in a new terminal
```bash
  celery -A dj_proj.celery worker --pool=solo -l info
```

Start the Celery beat in a new terminal
```bash
  celery -A dj_proj beat -l INFO
```


