#!/bin/bash

# Function to check if tmux is installed
check_tmux_installed() {
    if ! command -v tmux &> /dev/null; then
        echo "tmux is not installed. Installing tmux..."
        sudo apt-get update
        sudo apt-get install -y tmux
    else
        echo "tmux is already installed."
    fi
}

# Check if tmux is installed, and install if necessary
check_tmux_installed

# Start a new tmux session if not already running
if tmux has-session -t dev_session 2>/dev/null; then
    echo "tmux session 'dev_session' is already running."
else
    echo "Starting new tmux session 'dev_session'..."

    # Start a new tmux session
    tmux new-session -d -s dev_session

    # Start the Django development server in the first tmux window
    tmux send-keys -t dev_session "python3 manage.py runserver 0.0.0.0:8080" C-m

    # Create a new tmux window and start the Tailwind CSS watcher there
    tmux new-window -t dev_session
    tmux send-keys -t dev_session:1 "./tailwindcss -i static/src/input.css -o static/output.css --watch" C-m
fi

# Attach to the tmux session
tmux attach -t dev_session