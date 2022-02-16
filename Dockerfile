FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3-pip
RUN pip install Flask
ADD ./flask_application.py /src/flask_application.py
CMD ["python3", "/src/flask_application.py"]
