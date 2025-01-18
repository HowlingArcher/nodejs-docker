#!/usr/bin/env python3
import os
import subprocess
import time

# Change this to your filepath
template_filepath = "/home/admin/nodejs-docker/template.txt"

if not os.path.exists(template_filepath):
    print("Template File not found! Please change this in the 'create-docker-compose.py' file!")

# Get the current working directory (where the script is being run from)
current_dir = os.getcwd()

# Extract the folder name from the current working directory
folder_name = os.path.basename(current_dir)

folder_name = f"{folder_name}".lower()

print(f"Running script in folder: {folder_name}")

# Ask the user for the startup file name
startup_file = input("Please enter the startup file name (e.g., index.js): ")

# Ask if the person wants to enable a port
enable_port = input("Does this container require a port number? y/N")
if not enable_port:
	enable_port = "n"
if enable_port.lower() == "y":
	portnumber = input("What port does your code use?");
	dockerport = input("What port number do you want to access your program at?")
	if not portnumber:
		print("Missint a port you want to use")
		exit
	if not dockerport:
		print("Missing a port you want to use")
		exit
if enable_port.lower() == "n":
	print("Will not assign a port number")

# Define the placeholder and the new value
placeholder = "{{startupFile}}"
new_value = startup_file  # You can replace this with the actual startup file name

# Open the source template file and read its content
with open(template_filepath, "r") as file:
    content = file.read()

# Replace the placeholder with the new value
updated_content = content.replace(placeholder, new_value)

# Write the updated content to the new docker-compose.yml file
with open("Dockerfile", "w") as file:
    file.write(updated_content)

print("Placeholder replaced and content saved to docker-compose.yml!")

# Run the docker build command using the current directory as the image tag
docker_build_command = f"docker build -t {folder_name} ."

print(f"Running command: {docker_build_command}")
# Execute the docker build command
subprocess.run(docker_build_command, shell=True, check=True)

print("Docker image built successfully!")

docker_run_command = ""

# Run the docker run command
if enable_port == "n":
	docker_run_command = f"docker run -d --name {folder_name}-container {folder_name}"
if enable_port == "y":
	docker_run_command = f"docker run -d -p {dockerport}:{portnumber} --name {folder_name}-container {folder_name}"
print(f"Running command: {docker_run_command}")
subprocess.run(docker_run_command, shell=True, check=True)

print(f"Docker container should be up!")

docker_log_command = f"docker logs {folder_name}-container"

print(f"Running command: {docker_log_command}")

time.sleep(20)

subprocess.run(docker_log_command, shell=True, check=True)
