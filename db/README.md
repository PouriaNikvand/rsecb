# initializing database

this part is for initalizing the mongo database

###initialization :
You use `stack.yml` as a docker-compose file for running the mongodb for this, first go to db folder and run this command
```
docker-compose -f stack.yml up -d
```
this command uses mongo docker image and pull the image and runs it on your device.

you can check this for more options : [mongodb_image_link](https://hub.docker.com/_/mongo).

###import database
first you have to attach to the database container :
 ```
dokcer exec -it ContainerID bash
```
also for getting ContainerID you can use : 
```
docker ps
``` 
then import your initial database in mongo using this command : (test for DB name and taptap for Collection name)
```
mongoimport --authenticationDatabase admin -u root -p example --type csv -d test -c taptap --headerline --drop /ext_files/task-23-dataset.csv
```


now your database is ready with your data to use in port 27017