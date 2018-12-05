[![Coverage Status](https://coveralls.io/repos/github/larryTheGeek/iReporterApi/badge.svg?branch=develop)](https://coveralls.io/github/larryTheGeek/iReporterApi?branch=develop)
[![Build Status](https://travis-ci.com/larryTheGeek/iReporterApi.svg?branch=develop)](https://travis-ci.com/larryTheGeek/iReporterApi)

# iReporterApi
iReporter is an application whose aim is to reduce corruption in Africa and foster economic development. It allows users to create red flags and interventions. It implents the following list of APIs.

### Framework used
The application is built using python: flask framework.
>[Flask](http://flask.pocoo.org/) is a microframework for the Python programming language.


### End points
Method | Endpoint | Usage |
| ---- | ---- | --------------- |
|POST| `/api/v1/auth/register` |  Register a user. |
|POST| `api/v1/auth/login` | Login user.|
|POST| `api/v1/red-flags` | Create a new red-flag. |
|GET| `api/v1/red-flags` | Get all the created redflags. |
|GET| `api/v1/red-flags/<red_flag_id>` | Get a single redflag. |
|PATCH| `api/v1/red-flags/<red_flag_id>/location` | Update a single redflag location. |
|PATCH| `api/v1/red-flags/<red_flag_id>/comment` | Update a single redflag comment. |
|PATCH| `api/v1/red-flags/<red_flag_id>/status` | Update a single redflag status. |
|DELETE| `api/v1/red-flags/<red_flag_id>` | Delete a single redflag. |

## Installation 🕵
- To run on local machine git clone this project :
```
$ git clone https://github.com/larryTheGeek/iReporterApi.git
```
Copy and paste the above command in your terminal, the project will be downloaded to your local machine.

To Install python checkout:
```
https://www.python.org/
```

- create a virtualenv and make it use python 3 using the following command.
```
$ virtualenv -p python3 env
```
- activate the virtual environment
```
 $ source env/bin/activate
```
- Install Requirements
```
$ pip install -r requirements.txt
```
### Testing
- Run Test using pytest with the following command
```
$ py.test --cov=app test` 
```
you will get the test coverage report on your terminal


The app can also be tested via Postman
- Run App 
```
$ python run.py
```
The app should be accessiable via : http://127.0.0.1:5000/

open postman and navigate to the API endpoints described above

### HEROKU URL
 https://irepoter-afric-app.herokuapp.com/api/v1
 
### Owner
- Larry Karani




