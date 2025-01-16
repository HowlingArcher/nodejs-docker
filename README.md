# nodejs-docker
Make a nodejs project in docker work :) - automated?

## What is this?
This is a simple shell script that automates the process for me to create a docker container for my discord bots written in nodejs.

## How to use this?
You can use this script by copying this repo like this:
```git clone git@github.com:HowlingArcher/nodejs-docker.git```

CD into the repo folder: `cd nodejs-docker`

Change the template file path in the `create-docker-compose.py` file. Otherwise the script won't work and gives you an error that you need to change this.

Give the create-docker-compose.py file executable permissions like so:
```chmod +x create-docker-compose.py```

To use this script everywhere in your system (that's what it's made for) you can use this to make it globally accessable:
```sudo cp ./create-docker-compose.py /usr/local/bin/create-docker-compose```

Now you can use the `create-docker-compose` anywhere!

## How does it work?
The python script is simple, first it checks in what folder you're currently in and logs that in the console. Then it will ask you what your nodejs project startup file is. After that it will create the Dockerfile from the template.txt which you do need to define in the create-docker-compose.py file before copying it to the /usr/local/bin folder. 


After it has copied over the Dockerfile to your code, it will run the docker command `docker build -t {folder_name}` in where {folder_name} should be the name of the folder you used the program in. 


When that's done it runs the container with the command `docker run -d --name {folder_name}-container {folder_name}`


After it's done with that, it will wait 20 seconds and then runs a command to view the log of the server once with `docker logs {folder_name}_container`


Last the code will exit and you can run other commands again :) 
