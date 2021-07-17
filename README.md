# rsecb
Restfull Serve Estimated CTRs Backend

This project is a small webservice for serving a data from mongo and monitoring the performance.
all the project is dockerized and contains 3 parts:

- database (mongodb) in db folder
- webservice (python - tornado) in src folder
- exporters and monitoring systems (prometheus - graphana - ...) in exporter folder

Each folder has seprate docker-compose for running. use readme in each folder for running each part of the project.
als

| <sub>**Task**</sub> | <sub>**Active Time**</sub> | <sub>**Description**</sub> | 
| :--- | :--- | :--- |
| <sub>task initialization</sub>                    | <sub>1h</sub>      | <sub>reading and prepare the road map for doing the task </sub>
| <sub>READ mongodb</sub>                           | <sub>1h</sub>      | <sub></sub>
| <sub>READ tornado</sub>                           | <sub>1h</sub>      | <sub></sub>
| <sub>READ in memory caching</sub>                 | <sub>1h</sub>      | <sub></sub>
| <sub>READ unittest</sub>                          | <sub>2h</sub>      | <sub></sub>
| <sub>dao</sub>                                    | <sub>2h</sub>      | <sub></sub>
| <sub>rest api</sub>                               | <sub>5h</sub>      | <sub>api manager and cache management system</sub>
| <sub>docker</sub>                                 | <sub>1h</sub>      | <sub></sub>
| <sub>exporters</sub>                              | <sub>2h</sub>      | <sub></sub>
| <sub>unittest</sub>                               | <sub>2h</sub>      | <sub></sub>
| <sub>debug & chcek</sub>                          | <sub>1h</sub>      | <sub></sub>
|<sub>**--------------------------------**</sub>    | <sub>**----------**</sub> | <sub></sub>
| <sub>**TOTAL PROJECT**</sub>                      | <sub>**20h**</sub> | <sub></sub>
