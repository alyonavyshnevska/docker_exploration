# Definitions

- **Container** is a running instance of an image
- **Image** is a template for creating the environment you want. Snapshop of a system at a particular time
  - OS
  - Software
  - Application 
- Images are defined in a **Dockerfile**. When you run an image you get a container. 



Dockerfile    -----*build*--->  Image   ---*run*--->      Container


 **Virtual Machines vs. Docker**
- Docker shares a kernel. VMs each have its own kernel

# Writing a dockerfile
- Go to Dokerhub. Find an image you need. 
E.g. php official

- Simple Dockerfile:

FROM php:7.0-apache  
COPY src/ /var/www/html  
EXPOSE 80   

Download php. 
Copy our files from src/ to this location inside of the image.   
Tell running containers to listen on port 80. 
Output a new image -- which we will be able to run. 


# Commands

- `docker build -t hello-word . ` : build an image

    - -t  names the image "hello-world"
    - .  location of Dockerfile

- Run an instance of an image = a container
`docker run -p 80:80 hello-world`
first 80: local host.  
second 80: what docker container is listening to (in the Dockerfile: EXPOSE 80. (port).   

- Runs an instance of an image, exits. We don't see the container running. 

`docker stop name` : to stop running container

`docker rm name` : remove container permanently 

- Volumes: live changes 
mount local folder inside the container.  
`docker run -p 80:80 -v /Users/which/folder/to/mount:/var/www/html hello-world`

- `FROM python:3-onbuild`
installs requirements file

- `docker images` to list all images
- `docker rmi name` to remove an image. Make sure no container is running off that image

- `docker pull`: pulls an image, stores it on host, doesn't run the container

- `docker exec name command`: execute action inside a container

- `docker run -d name` : run container in a detached mode. Container continues to run in the background, access to terminal 
    - `docker attack id` : back to the detached container

- `docker container stop $(docker container ls -aq)` stop all containers
    - same for rm  


# docker-compose.yml
- specifies what you would otherwise say with docker build and docker run 
- one dir above the docker file
- `docker-compose up` from a dir where `docker-compose.yml` lives. Builds, runs everything

- `docker-compose build --no-cache`. 
if was a dummy and misspelt api.py

- Detached mode. In the background. can still use terminal:
`docker-compose -d`
- to ctrl+c: `docker-compose stop` 


# Commands
`docker ps` : list all running containers
`docker ps -a` : list all containers running or previously stopped
