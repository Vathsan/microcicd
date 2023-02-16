FROM python:3.9

WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir flask
RUN pip install -i https://test.pypi.org/simple/ wilo-cloud==4.0.0

ENV FLASK_APP=helloWorld
EXPOSE 5000
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]