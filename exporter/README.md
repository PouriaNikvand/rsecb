# initializing exporters

this part is for initalizing the exporters for monitoring our service

###initialization :
You use `prommaster.yml` as a docker-compose file for running the mongodb for this, first go to exporter folder and run this command
```
docker-compose -f prommaster.yml up -d
```

this command uses different images that contains prometheus - graphana - and some exporters. It pulls the images and run them on your device.

now your monitoring tools are ready and you can use them as you want

more details about running services & their ports:

graphana : exposed on port 3000 
prometheus : exposed on port 9090
nodexporter : exposed on port 9100
mongodbexporter : exposed on port 9216

for future works also alertmanager is available for monitoring and in graphana we needs to create proper dashboards.  