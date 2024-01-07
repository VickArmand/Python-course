#!/usr/bin/env bash
# Sends a POST request with data.
curl -sX POST -d "email=johndoe@gmail.com&username=johndoe123" 0.0.0.0:5000/add
# OR
curl -s -d "email=johndoe@gmail.com&username=johndoe123" 0.0.0.0:5000/add
# Sends a JSON POST request to a given URL with a given JSON file.
curl -s -X POST -H "Content-Type: application/json" -d "$(cat user.json)" 0.0.0.0:5000/add
# OR
curl -s -X POST -H "Content-Type: application/json" -d @user.json 0.0.0.0:5000/add