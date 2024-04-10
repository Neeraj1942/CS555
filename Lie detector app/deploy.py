# deploy.py
import os
import subprocess

# Build the app
subprocess.run(["python", "build.py"])

# Create a release
release_version = "1.0.0"
subprocess.run(["git", "tag", release_version])
subprocess.run(["git", "push", "origin", release_version])

# Deploy the app to production
subprocess.run(["ansible-playbook", "production_deploy.yml"])