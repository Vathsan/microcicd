FROM python:3.9

WORKDIR /usr/src/app

#COPY src/main/python/helloWorld.py ./

#COPY startup.sh ./

#RUN python -m venv envflask
#RUN source /envflask/bin/activate

RUN pip install --upgrade pip
RUN pip install --no-cache-dir flask
RUN pip install -i https://test.pypi.org/simple/ wilo-cloud==3.0.0

#RUN chmod +x startup.sh

ENV FLASK_APP=helloWorld
EXPOSE 5000
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
#CMD ["flask --app helloWorld run"]
#ENTRYPOINT ["/bin/bash", "startup.sh"]