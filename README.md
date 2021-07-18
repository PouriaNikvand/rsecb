# rsecb
Restfull Serve Estimated CTRs Backend

This project is a small webservice for serving a data from mongo and monitoring the performance.
All the project is dockerized and contains 3 parts:

- Database (mongodb) in db folder
- Webservice (python - tornado) in src folder
- Exporters and monitoring systems (prometheus - graphana - ...) in exporter folder

Each folder has seprate docker-compose for running. Use readme in each folder for running each part of the project.
Also run with the order of first build and run the **db** and then main docker-compose in rsecb folder for webservice
and then run the exporters.

### RSECB Service
This part is the main webservice using python - tornado. 
The code structure is a manage.py file and src folder containing these parts :
- Adaptors : the adaptoprs for calling api valid urls and handling the RequestHandler for tornado
- Arch : any important and using architecture. in this part we used Singleton
- Config : the base and running configs and constants for running the service
- DAO : the database access object which provides the access to the mongodb database and the methods for accessing database
- Manager : the main manager of running this project like the cache manager file and api manager. the cache manager is
the one who create a thread and update the in memory cache database from mongodb and the api manager is who 
call and run the main task for returning the results for the specific paths that defined as the valid webservice urls 
- Test : the unit test are in this folder - the tests are still not completed and need more works
- Utils : this part is not used yet in this project. (just my sample for project architecture)

### Working Schedule

| <sub>**Task**</sub> | <sub>**Active Time**</sub> | <sub>**Description**</sub> | 
| :--- | :--- | :--- |
| <sub>task initialization</sub>                    | <sub>1h</sub>      | <sub>reading and prepare the road map for doing the task </sub>
| <sub>READ mongodb</sub>                           | <sub>1h</sub>      | <sub>get ready for hands on mongodb</sub>
| <sub>READ tornado</sub>                           | <sub>1h</sub>      | <sub>get ready for hands on tornado</sub>
| <sub>READ in memory caching</sub>                 | <sub>1h</sub>      | <sub>get ready for using in memory caching system</sub>
| <sub>READ unittest</sub>                          | <sub>2h</sub>      | <sub>get ready for using unittest in the project</sub>
| <sub>dao</sub>                                    | <sub>2h</sub>      | <sub>data access objects developments</sub>
| <sub>rest api</sub>                               | <sub>5h</sub>      | <sub>api manager and cache management system</sub>
| <sub>docker</sub>                                 | <sub>1h</sub>      | <sub>write proper dockerfile and docker-compose for dockerizing the projct</sub>
| <sub>exporters</sub>                              | <sub>2h</sub>      | <sub>prepare exporters for monitoring the project (dockerizing and configs)</sub>
| <sub>unittest</sub>                               | <sub>2h</sub>      | <sub>unittest developments</sub>
| <sub>debug & check & reformatting</sub>           | <sub>3h</sub>      | <sub>refactoring the code and check and debug for each methods</sub>
|<sub>**--------------------------------**</sub>    | <sub>**----------**</sub> | <sub></sub>
| <sub>**TOTAL PROJECT**</sub>                      | <sub>**21h**</sub> | <sub></sub>


#### Don't hesitate to contact me for further improvements.