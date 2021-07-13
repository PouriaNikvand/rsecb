FROM python:3.8.4-slim-buster

# File Author / Maintainer
MAINTAINER P.Nikvand

# change time zone to Asia/Tehran
#RUN echo "Asia/Tehran" > /etc/timezone
#RUN rm -rf /etc/localtime
#RUN apt -y install tzdata

RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get install -y --no-install-recommends vim htop

RUN mkdir /app
WORKDIR /app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY rsecb ./rsecb

# Start processes
CMD ["python3", "-m","manage.py"]
#CMD ["tail", "-f","/dev/null"]