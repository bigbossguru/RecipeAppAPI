# RecipeAppAPI

## Recipe Backend Application REST API using Django REST Framework, Docker, GitHub Actions

<br>

### Build docker compose

```
docker compose build
```

### Build Dockerfile container

```
docker build .
```

### Set linting Flake8 settings and init

```
docker compose run --rm app sh -c "flake8"
```

### Create django project inside docker compose

```
docker compose run --rm app sh -c "django-admin startproject app ."
```

### Run Django tests from docker compose

```
docker compose run --rm app sh -c "python manage.py test"
```

### Run docker compose

```
docker compose up
```
