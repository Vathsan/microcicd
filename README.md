# Building and Deploying a Microservices Application on a Hybrid Cloud

1. Create a python virtual environment and activate it
2. Setup the following modules using pip:

    * `pip install pybuilder`
    * `pip install setuptools wheel twine`
    * `Pip install Flask`

3. Create a pybuilder project by executing  the command *`pyb --start-project`*.
  
   Use the following values to create a basic project structure.

    * Project name: `hospitalService`
    * Use the `default` values for Source, Docs, Unittest and Scripts directories
    * Since we are not going to use **flake8** and **coverage** plugins, type `‘n’`. For **distutils** type `'y'`(this is important to successfully build the project)

4. Refer to https://packaging.python.org/en/latest/guides/using-testpypi/ and register for a TestPyPI account. Once registered, generate an API token by following https://test.pypi.org/help/#apitoken

5. Now it's time to build and publish our application to Test Python Package Index. 

  To build the application run `pyb` from the root of your project. This generates the `target/dist` directory. Navigate to `target/dist/hospitalService-1.0.0/dist` to see the generated binary wheel and gzip’ed tar. 
  
  From here, execute `twine upload --repository testpypi *` to upload your distributions to TestPyPI using twine. Use the following when prompted for credentials,

    - username: `__token__ `
    - password: apitoken obtained in step 4

  You can see if your package has successfully uploaded by navigating to the URL https://test.pypi.org/project/hospitalService. Note that the hospitalService is the name of our project.

6. Let's use Docker to containerize our application. You can find a Dockerfile with related configurations in the root of the project. You may refer to https://docs.docker.com/engine/reference/builder/ to learn more about the syntax.

  Modify line 7 to download and install the application that we published to the PyPI index in previous step

7. Install Docker by referring to https://docs.docker.com/get-docker/ 

  Once installed, from the root of the project, execute `docker build -t hospital_service:1.0.0 .` to build and tag a docker image by reading the instructions from the Dockerfile.

8. Let's see how we can deploy our containerized application on a Hybrid Cloud, AWS EKS. To begin with, we need to create an EKS cluster. Follow the below steps to setup the cluster.







