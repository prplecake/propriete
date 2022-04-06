[![codecov](https://codecov.io/gh/prplecake/propriete/branch/master/graph/badge.svg?token=OP3YLKULU0)](https://codecov.io/gh/prplecake/propriete)

# propriete

A home inventory tracking system.

## Developing

A virtualenv is recommended.

```text
pip install -r requirements.txt
```

**Note:** The development requirements are only necessary when
recreating the ERD.

### Database Migrations

Creating migrations:

```text
python manage.py makemigrations
```

Applying migrations:

```text
python manage.py migrate
```

### Unit Tests

Running tests:

```text
python manage.py test
```

Increase verbosity:

```text
python manage.py test -v2
```

Running tests with coverage:

```text
coverage run --source='.' manage.py test
```

Generate HTML output:

```text
coverage html
```

Then open `htmlcov/index.html` to view report.
