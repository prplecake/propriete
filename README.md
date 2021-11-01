# propriete

A home inventory tracking system.

## Developing

**Requirements:**

* pipenv

```
pipenv install
pipenv run python manage.py migrate
pipenv run python manage.py runserver
```

**Note:** The development requirements are only necessary when
recreating the ERD.

### Database Migrations

Creating migrations:

	pipenv run python manage.y makemigrations

Applying migrations:

	pipenv run python manage.py migrate

### Unit Tests

Running tests:

	pipenv run python manage.py test

Increase verbosity:

	pipenv run python manage.py test -v2

Running tests with coverage:

	pipenv run coverage run --source='.' manage.py test

Generate HTML output:

	pipenv run coverage html

Then open `htmlcov/index.html` to view report.

## Data Model

![](https://drop.jrgnsn.net/_Lbf.png)

Generate a new data model:

	pipenv run python manage.py graph_models -o db_graph.png inventory media meta
