@echo off
cls 
title Installing Python Modules. . .
python get-pip.py
pip install -r requirements.txt
echo Done! You Can Close This And Open The Python File.
pause