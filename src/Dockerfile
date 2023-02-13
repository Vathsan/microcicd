FROM python:3.9

WORKDIR /usr/src/app

#COPY src/main/python/helloWorld.py ./
COPY ../target/dist/wilo_cloud-1.0.dev0/dist/wilo_cloud-1.0.dev0-py3-none-any.whl ./

#COPY startup.sh ./

#RUN python -m venv envflask
#RUN source /envflask/bin/activate

RUN pip install --upgrade pip
RUN pip install --no-cache-dir flask
RUN pip install wilo_cloud-1.0.dev0-py3-none-any.whl

#RUN chmod +x startup.sh

ENV FLASK_APP=helloWorld
EXPOSE 5000
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
#CMD ["flask --app helloWorld run"]
#ENTRYPOINT ["/bin/bash", "startup.sh"]