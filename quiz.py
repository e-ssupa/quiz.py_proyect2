from time import sleep

while True:
    print("\nWelcome to the TRUE quiz to test if you're the next Albert Einstein!\n")
    sleep(1.6)
    print("You must answer 25 questions to prove your intelligence.")
    sleep(1.6)
    
    startgame = input("Wanna test if you're really Einstein? (Y/N): ").upper().strip()
    if startgame not in ("YES", "Y"):
        sleep(1.5)
        print("\nok")
        break
    else:
        print('Inputting the questions..')
        sleep(2)

    questions = (
        "What is the SECOND most spoken language in the United States of America?",
        "5 to the power of 10?",
        "What is the biggest continent in the world?",
        "What is the most used dedicated AI app in the world?",
        "What modern-day country started World War 2?",
        "A loaf of bread costs 12 dollars. How much would you have to pay if you bought 1376?",
        "Most expensive company in the world?",
        "You have 1,079,532 dollars, but i stole 37 percent of it, how much did i?",
        "How many questions were there so far? (Not including this)",
        "Which planet in our solar system is known for its massive, visible rings?",
        "What is the chemical symbol for gold?",
        "How many bones are there in an adult human body?",
        "Which ocean is the largest and deepest on Earth?",
        "Who painted the famous artwork 'The Starry Night'?",
        "What is the square root of 225?",
        "Which country gifted the Statue of Liberty to the United States?",
        "What is the fastest land animal in the world?",
        "Which fundamental force keeps us on the ground?",
        "Which organ in the human body consumes the most energy?",
        "What year did Albert Einstein win the Nobel Prize in Physics?",
        "What does the 'c' stand for in Einstein's famous equation E=mc²?",
        "Which particle has a negative charge?",
        "What is the closest star to Earth?",
        "How many elements are on the periodic table?",
        "Which gas makes up the majority of Earth's atmosphere?"
    )

    options = (
        ("A: French", "B: Spanish", "C: Chinese", "D: German"),
        ("A: 9,765,625", "B: 1,562,500", "C: 50,000,000", "D: 4,882,812"),
        ("A: Africa", "B: North America", "C: Asia", "D: Antarctica"),
        ("A: Midjourney", "B: Claude", "C: DeepSeek", "D: ChatGPT"),
        ("A: Italy", "B: Germany", "C: Japan", "D: Russia"),
        ("A: $15,212", "B: $16,512", "C: $17,812", "D: $16,200"),
        ("A: Apple", "B: Microsoft", "C: Nvidia", "D: Alphabet"),
        ("A: $399,426.84", "B: $411,200.50", "C: $387,950.00", "D: $365,400.12"),
        ("A: 6", "B: 7", "C: 8", "D: 9"),
        ("A: Mars", "B: Jupiter", "C: Saturn", "D: Neptune"),
        ("A: Go", "B: Gd", "C: Ag", "D: Au"),
        ("A: 186", "B: 206", "C: 216", "D: 296"),
        ("A: Atlantic Ocean", "B: Indian Ocean", "C: Arctic Ocean", "D: Pacific Ocean"),
        ("A: Leonardo da Vinci", "B: Vincent van Gogh", "C: Pablo Picasso", "D: Claude Monet"),
        ("A: 12", "B: 15", "C: 25", "D: 35"),
        ("A: France", "B: United Kingdom", "C: Canada", "D: Italy"),
        ("A: Cheetah", "B: Pronghorn", "C: Lion", "D: Peregrine Falcon"),
        ("A: Magnetism", "B: Centrifugal Force", "C: Friction", "D: Gravity"),
        ("A: Heart", "B: Liver", "C: Brain", "D: Kidneys"),
        ("A: 1905", "B: 1915", "C: 1921", "D: 1933"),
        ("A: Constant", "B: Speed of light", "C: Conductivity", "D: Centripetal force"),
        ("A: Proton", "B: Neutron", "C: Electron", "D: Quark"),
        ("A: Proxima Centauri", "B: Alpha Centauri", "C: Sirius", "D: The Sun"),
        ("A: 92", "B: 108", "C: 115", "D: 118"),
        ("A: Oxygen", "B: Nitrogen", "C: Carbon Dioxide", "D: Hydrogen")
    )

    answers = ("B", "A", "C", "D", "B", "B", "C", "A", "C", "C", "D", "B", "D", "B", "B", "A", "A", "D", "C", "C", "B", "C", "D", "D", "B")
    
    guesses = []
    score = 0
    question_num = 0
    total_questions = len(questions)

    for question in questions:
        while True:
            print("\n! - - / - - !")
            print(question)
            for option in options[question_num]:
                print(option)
            
            guess = input("Enter your choice answer: A... B... C... D... ").upper().strip()
            if guess in ("A", "B", "C", "D"):
                guesses.append(guess)
                break
            else:
                print("\nInvalid symbol. Please enter only A, B, C, or D.\n")
                sleep(1.5)

        if question_num == total_questions - 1:
            if guess == answers[question_num]:
                score += 1
                print("That's correct buddy!")
            else:
                print("Wrong answer.")
                print(f"I think it was {answers[question_num]} .....")
            
            print("\nAnd that's everything we need to test; Calculating your IQ...")
            sleep(1)
            print("Checking your answers...")
            sleep(1)
            print("Calculating your intelligence...")
            sleep(1)
            print("Collecting the last information...")
            sleep(0.5)
            
        elif guess == answers[question_num]:
            score += 1
            print("That's correct buddy! And to move on..")
            sleep(1.25)
        else:
            print("Wrong answer.")
            print(f"I think it was {answers[question_num]} ...")
            sleep(1.25)

        if question_num == 8:
            print("\nInto to the second wave of questions we go...\n")
            sleep(2.0)

        question_num += 1

    percentage = int((score / total_questions) * 100)
    
    if score == total_questions:
        einstein_status = "You're Einstein"
    elif score >= 18:
        einstein_status = "Halfway through Einstein"
    elif score >= 10:
        einstein_status = "Tiny bit of Einstein"
    else:
        einstein_status = "Not Einstein"

    print("\n- - - RESULTS - - -")
    print(f"| Out of {total_questions} questions, you answered {score} of them correctly.")
    print(f"| You are {percentage}% Albert Einstein!")
    print(f"| Verdict: {einstein_status}.\n")
    sleep(2.5)

    play_again = input("Do you desire a retest of your Einstein skills? (YES/NO): ").upper().strip()
    if play_again not in ("YES", "Y"):
        sleep(1.5)
        print("\nAt least you have tested if you were Albert Einstein. Goodbye mister/miss Einstein.")
        break
