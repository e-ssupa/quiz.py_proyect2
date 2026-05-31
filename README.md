## EXPLANATION
This is a quiz game you can use in the console to test your general knowledge and see if you are the next Albert Einstein. It is written in Python as part of my learning journey and is really easy to run and play

## Features

* Multi-wave progression system: The quiz contains 25 intense questions split into stages, featuring an integrated transition indicator message when you pass the first wave.
* Strict input validation loop: The program checks your choices carefully. If you type an invalid symbol, it won't skip the question or break; it will loop until you give a valid response.
* Custom status generator: It dynamically calculates your right choices, converts them into a percentage, and assigns an overall intelligence tier (Einstein status).
* Playback looping system: The script lets you instantly restart the game to retest your skills, or you can shut it down gracefully.

## Requirements

* Python 3.x

## How to Install Python## Windows

   1. Download the installer from the official page: python.org/downloads.
   2. Open the downloaded .exe file.
   3. Check the box "Add python.exe to PATH" at the bottom before clicking install.
   4. Click Install Now.

## macOS

brew install python

## Linux (Ubuntu/Debian)

sudo apt update && sudo apt install python3 -y

## To check if it works

python --version

## Installation and Running
Download the quiz.py file. Open the terminal or command prompt, navigate to the folder, and run the script:

cd "C:\Users\Windows 10 Pro\Desktop\Python proyects\quiz"
python quiz.py

## How to Use

   1. Read the question prompt displayed between the ! - - / - - ! lines.
   2. Look at the options list (A, B, C, D).
   3. Type your choice letter and press Enter.
   4. At the end, choose YES to play again or anything else to say goodbye.

## What's in the code?

* while True main loop handles the playback system so you can restart the entire test.
* questions, options, and answers are structured tuples that store all data securely.
* guess in ('A', 'B', 'C', 'D') performs strict input validation inside a secondary loop.
* if question_num == 8: triggers the transition warning to announce the second wave of questions.
* einstein_status evaluates your end score to classify your Einstein status tier.
