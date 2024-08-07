#!/bin/bash

# Install Python
sudo apt-get update
sudo apt-get install -y python3 python3-pip

# Create a new Python virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Initialize a new Python project
mkdir project
cd project

# Install Flask
pip install flask

# Install other dependencies (if any)
pip install -r requirements.txt

# Run the Flask application
python app.py