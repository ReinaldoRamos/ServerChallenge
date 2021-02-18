# ServerChallenge

## Overview

This project contains an API made with python 3 & a simple html/javascript frontpage for consulting alerts in servers. This still under development.

## Instructions

For this project we will run the environment using Docker, in order to prevent differences between local configurations.

1) Get Docker for your system in https://www.docker.com/

2) After instalation, make sure the app is running, then execute the following command in your terminal from ~./devtools/:
```bash
docker-compose up
```
 * On Windows you may need to index system variables to run this.
 * Make sure there's no other service using port 8080 so there are no conflicts.

3) This will create a local server in https://0.0.0.0:8080 using nginx in a container. 

4) You can access the API documentation in https://0.0.0.0:8080/docs after the build is complete.

5) You can make some tests to see if everything is fine running the teste_challenge.sh in the same repository.
- Grant permissions for the file:
```bash
cmod +x teste_challenge.sh
```
- Then run this in your terminal:
```bash
./teste_challenge.sh
```

