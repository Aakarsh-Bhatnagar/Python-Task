FROM python:3.7
ADD main.py /aakarsh/
ADD task.py /aakarsh/
RUN apt-get update && apt-get install vim -y
RUN pip install pymongo 
