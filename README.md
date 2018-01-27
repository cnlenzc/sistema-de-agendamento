# REST API for scheduling system

This project is an application that provides an API for handling a scheduling system

## Getting Started

These instructions will get you a copy of the project up and running on your local machine
 for development and testing purposes.
See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

* Python 3.6+
* Postgre 10+
* Heroku free account


### Installing

A step by step series to get a development env running

Clone de project
```
$ git clone https://github.com/cnlenzc/sistema-de-agendamento.git
```

Create a Python virtualenv and install dependencies from Pipfile
```
$ cd sistema-de-agendamento
$ pipenv install
$ pipenv shell
```

Set environment variables by create .env file
```
$ export DATABASE_URL='postgres://{{username}}:{{password}}@localhost:port/{{database}}'
```
Example of sistema-deagendamento/.env file:
```
WEB_CONCURRENCY=2
DATABASE_URL='postgresql://u_age:pwd123@localhost:5432/db_age'
```

Create the database objects
```
$ python manage.py migrate
```

Import data from test
```
$ python manage.py import ...
```

## Running the automatic tests

How to run the automated tests for this system
```
$ python manage.py test
```
Result
```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
........................
----------------------------------------------------------------------
Ran 24 tests in 0.972s

OK
Destroying test database for alias 'default'...
```

## Using the API

You can use the API by internet with these URL

###### API Documentation
https://sistema-de-agendamento-lenz.herokuapp.com/docs

###### Hello World page
https://sistema-de-agendamento-lenz.herokuapp.com


### Coding style tests

Explain what these tests test and why

```
Not yet implemented
```

## Deployment by heroku

How to deploy this on a live system
```
$ git add .
$ git commit -m "Added a file"
$ heroku login
    Enter your Heroku credentials…
$ heroku create
    Creating app... done, ⬢ nameless-fortress-70834
    https://nameless-fortress-70834.herokuapp.com/ | https://git.heroku.com/nameless-fortress-70834.git
$ git push heroku master
    -----> Python app detected
    -----> Launching... done, v7
```

## Built With

* [Python](https://www.python.org) - The programming language used
* [Django](https://www.djangoproject.com) - The web framework used
* [Django Rest Framework](http://www.django-rest-framework.org) - The API REST framework used
* [Postgres.app](http://postgresapp.com/documentation/) - The SQL DataBase used
* [Heroku](https://devcenter.heroku.com/categories/python) - Used to deploy and cloud

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

```
Not yet implemented
```

## Authors

* **Carlos Neves Lenz Cesar** - *Initial work*

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Heroku Docs
* Rest Django Framework Docs
* Django Docs
* You, who have read this document to the end
