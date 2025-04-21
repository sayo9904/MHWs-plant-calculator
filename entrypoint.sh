#!/bin/bash


pip install --upgrade pip
pip install -r requirements.txt

if [ ! -d "log" ]; then
	mkdir log
fi
