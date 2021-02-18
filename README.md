# ServerChallenge

## Overview

This project contains an API made with python 3 & a simple html/javascript frontpage for consulting alerts in servers. This still under development.

## Getting started

For this project we will run the environment using Docker, in order to prevent differences between local configurations.

1) Get Docker for your system in https://www.docker.com/

2) After instalation, make sure the app is running, then execute the following command in your terminal from ~./devtools/challenge/:
```bash
docker-compose up
```
   PS.: * On Windows you may need to index system variables to run this.
        * Make sure there's no other service using this port so there are no conflicts.

3) This will create a local server in https://0.0.0.0:8080 using nginx in a container. 

