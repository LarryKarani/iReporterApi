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

[![Coverage Status](https://coveralls.io/repos/github/larryTheGeek/iReporterApi/badge.svg?branch=develop)](https://coveralls.io/github/larryTheGeek/iReporterApi?branch=develop)
