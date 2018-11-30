# iReporterApi
iReporter is an application whose aim is to reduce corruption in Africa and foster economic development. It allows users to create red flags and interventions. It implents the following list of APIs.

Method | Endpoint | Usage |
| ---- | ---- | --------------- |
|POST| `/api/v1/signup` |  Register a user. |
|POST| `api/v1/login` | Login user.|
|POST| `api/v1/redflags` | Create a new red-flag. |
|GET| `api/v1/redflags` | Get all the created redflags. |
|GET| `api/v1/redflag/<red_flag_id>` | Get a single redflag. |
|PATCH| `api/v1/redflag/<red_flag_id>/location` | Update a single redflag location. |
|PATCH| `api/v1/redflag/<red_flag_id>/comment` | Update a single redflag comment. |
|PATCH| `api/v1/redflag/<red_flag_id>/status` | Update a single redflag status. |
|DELETE| `api/v1/redflag/<red_flag_id>` | Delete a single redflag. |



[![Build Status](https://travis-ci.com/larryTheGeek/iReporterApi.svg?branch=develop)](https://travis-ci.com/larryTheGeek/iReporterApi)

<a href="https://codeclimate.com/github/larryTheGeek/iReporterApi/maintainability"><img src="https://api.codeclimate.com/v1/badges/55f6147ce61b0772db62/maintainability" /></a>
<a href="https://codeclimate.com/github/larryTheGeek/iReporterApi/test_coverage"><img src="https://api.codeclimate.com/v1/badges/55f6147ce61b0772db62/test_coverage" /></a>

## Getting Started 🕵
- To run on local machine git clone this project :
```
$ git clone https://github.com/larryTheGeek/iReporterApi.git
```
Copy and paste the above command in your terminal, the project will be downloaded to your local machine.

### Prerequisites
The application is built using python: flask framework.
>[Flask](http://flask.pocoo.org/) is a microframework for the Python programming language.


To Install python checkout:
```
https://www.python.org/
```
### Installing
For this section I will assume you have python3 and it's configured on your machine. </br>
Navigate to the folder you cloned and run: </br>

- Install Requirements
```
$ pip install -r requirements.txt
```
- Run App 
```
$ python run.py
```
The app should be accessiable via : http://127.0.0.1:5000/

