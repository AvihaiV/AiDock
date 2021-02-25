# AiDock
Home Assignment

Creating a Dockerfile to create an image that will run Python script on Ubuntu machine.

1.	Make sure Docker is installed on your machine and you are able to run Docker commands.
2.	Run 
```
$docker build -t devops .
```
3.	This will create the image and all the relevant dependences to run this task.
4.	If you wish to install Jenkins and configure all the required steps to run docker on Jenkins and creating the Users and Groups needed please run the second   Dockerfile, Dockerfile-Jenkins
5.	In the Jenkins Folder run:
```
docker build -t jenkins . 
```
7.	In order to configure Jenkins, you need to run the docker-compose.yml file, this will create all the relevant volumes and ports.
8.	Run:
```
docker-compose up
```
9.	Once Jenkins is installed you can copy both Jenkinsfile and create two Jenkins Pipelines, One scripted and one declarative.
10.	Copy the Jenkins file to its respectful pipeline.
 
