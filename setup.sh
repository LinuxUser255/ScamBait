#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if python3 and pip3 are installed
if ! command_exists python3 || ! command_exists pip3; then
    echo "Error: Python3 and pip3 are required but not installed."
    exit 1
fi

# Prompt user about virtual environment
read -p "Do you want to create and activate a virtual environment? (y/n): " create_venv

if [[ $create_venv =~ ^[Yy]$ ]]; then
    # Check if venv module is available
    if ! python3 -m venv --help > /dev/null 2>&1; then
        echo "Error: Python3 venv module is not available. Please install it and try again."
        exit 1
    fi

    # Create and activate virtual environment
    python3 -m venv venv
    source venv/bin/activate

    echo "Virtual environment created and activated."
else
    echo "Proceeding without virtual environment."
fi

# Update pip3
echo "Updating pip3..."
pip3 install --upgrade pip

# Check if requirements.txt exists
if [ -f "requirements.txt" ]; then
    # Install requirements
    echo "Installing requirements from requirements.txt..."
    pip3 install -r requirements.txt
else
    echo "Warning: requirements.txt not found. Skipping package installation."
fi

echo "Setup complete!"
