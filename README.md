# Python Django API Service Boilerplate

This boilerplate provides ready to use code to start developing web service using python and django rest framework.

## Lib details:
|Name|Details/Version|
|-----|----|
|Python|3.8|
|Django|3.0.5|
|djangorestframework|3.11.0|
|Database support|postgresql|
|virtualenv||

## Getting started
You can directly use this boilerplate and replace name of this project with your project name. But you need `SECRET_KEY` for your project. `SECRET_KEY` is unique to each project and this project has its own key which won't work for your project.

So first create normal django project and take all contents from this boilerplate to your project!

**NOTE:** Please make sure in your real project don't store `SECRET_KEY` in source code, use some `env` variable and pass value through it.

## How to run:

### For development

- Install `virtualenv`
- After installing, create virtual env by `virtualenv venv` in *root of project*
- Activate env by `source ./venv/bin/activate` (for MAC)
- Install dependencies by `pip install -r requirements.txt`

  **NOTE:** If you are using mac, installing `psycopg2-2.8.5` may fail. Then manually install it using this command:
            `env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip3.8 install psycopg2`
- Make sure your DB Server is running and *you already created database*, and use following to migrate (Create tables):
  - `python manage.py makemigrations`
  - `python manage.py migrate`
- Start dev server: `python manage.py runserver` 🎉

### For production

Docker configuration with `nginx` is already set up with this boilerplate.

You need to set some `env` variables for e.g. `APP_ENV=prod`, `DB_NAME=xxxx` etc.

Just do `docker-compose up -d` and your server will be running! 🎉

## Testing

Beauty of django tests I felt is, it's easy to write and it automatically creates *test database* during test and also destroys after test.

Anyway to test I recommend first you check current coverage of project and know what is already tested and what is not. Don't repeat yourself!!

`coverage run --omit='*/venv/*' manage.py test`

Get coverage report with:

`.coverage report`

and you can also generate HTML Report:

`.coverage html`

Now there is already super simple test under `scheduler/tests` directory. And to test that just run:

`python manage.py test scheduler`

## Swagger UI

Swagger UI is also configured. Goto `http://yourhost:port/swagger-ui/`

## Future work to do:
- Set up `pylint`
- Improve security in `nginx`
