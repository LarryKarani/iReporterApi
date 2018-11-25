# iReporterApi
iReporter is an application whose aim is to reduce corruption in Africa and foster economic development. It allows users to create red flags and interventions. It implents the following list of APIs

Method | Endpoint | Usage |
| ---- | ---- | --------------- |
|POST| `/iReporter/api/v1/signup` |  Register a user. |
|POST| `/iReporter/api/v1/login` | Login user.|
|POST| `/iReporter/api/v1/redflags` | Create a new red-flag. |
|GET| `/iReporter/api/v1/redflags` | Get all the created redflags. |
|GET| `/iReporter/api/v1/redflag/<red_flag_id>` | Get a single redflag. |
|PUT| `/iReporter/api/v1/redflag/<red_flag_id>` | Update a single redflag. |
|DELETE| `/iReporter/api/v1/redflag/<red_flag_id>` | Delete a single redflag. |

