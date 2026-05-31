## EXPLANATION
This is a quiz game you can use in the console to test your general knowledge and see if you are the next Albert Einstein. It is written in Python as part of my learning journey and is really easy to run and play
## Features

* Multi-wave progression system: The quiz contains 19 intense questions split into stages, featuring an integrated transition indicator message when you pass the first wave.
* Strict input validation loop: The program checks your choices carefully. If you type an invalid symbol, it won't skip the question or break; it will loop until you give a valid response.
* Custom status generator: It dynamically calculates your right choices, converts them into a percentage, and assigns an overall intelligence tier (Einstein status).
* Playback looping system: The script lets you instantly restart the game to retest your skills, or you can shut it down gracefully.

------------------------------
## How to Install Python
You need Python 3 installed on your computer to run this game.
## Windows

   1. Download the installer from the official page: python.org/downloads.
   2. Open the downloaded .exe file.
   3. Important: Make sure to check the box "Add python.exe to PATH" at the bottom before clicking install.
   4. Click Install Now.

## macOS

   1. Open your terminal application.
   2. Run the Homebrew command:
   
   brew install python
   
   (Or download the macOS package directly from python.org).

## Linux (Ubuntu/Debian)

   1. Open your terminal.
   2. Run this command to update packages and install Python:
   
   sudo apt update && sudo apt install python3 -y
   
   
## To check if it works
Open a new terminal window and type:

python --version

------------------------------
## Installation and Running
Download the quiz.py file. Open the terminal or command prompt, navigate to the folder, and run the script:

cd "C:\Users\Windows 10 Pro\Desktop\Python proyects\quiz"
python quiz.py

## How to Use
The quiz will run automatically and ask you multiple-choice questions, here’s what you need to do:

   1. Read the question prompt displayed between the ! - - / - - ! lines.
   2. Look at the options list (A, B, C, D).
   3. Type your choice letter and press Enter.
   4. If you make a mistake, don't worry, the program will ask you to enter only valid choices.
   5. At the end, choose YES to play again or anything else to say goodbye.

## What's in the code?

* while True main loop handles the playback system so you can restart the entire test.
* questions, options, and answers are structured tuples that store all data securely.
* guess in ('A', 'B', 'C', 'D') performs strict input validation inside a secondary loop.
* if question_num == 8: triggers the transition warning to announce the second wave of questions.
* einstein_status evaluates your end score to classify if you are a "Tiny bit of einstein", "Halfway through einstein", or if "You're einstein".
