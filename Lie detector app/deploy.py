# deploy.py
import os
import subprocess

# Building the application
subprocess.run(["python", "build.py"])

# Creating a release
release_version = "1.0.0"
subprocess.run(["git", "tag", release_version])
subprocess.run(["git", "push", "origin", release_version])

# Deploying the app to the production
subprocess.run(["ansible-playbook", "production_deploy.yml"])
