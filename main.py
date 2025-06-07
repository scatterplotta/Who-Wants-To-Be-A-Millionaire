import random
import time
import sys

class MillionaireGame:
    def __init__(self):
        self.money_levels = [
            100, 200, 300, 500, 1000, 2000, 4000, 8000, 
            16000, 32000, 64000, 125000, 250000, 500000, 1000000
        ]
        
        self.lifelines = {
            "50/50": True,
            "Phone a Friend": True,
            "Ask the Audience": True
        }
        
        self.current_question = 0
        self.current_winnings = 0
        
        # Track used questions to prevent repeats
        self.used_questions = set()
        
        # Question bank organized by difficulty and theme
        self.questions = {
            # Easy questions (1-5)
            1: [
                {"theme": "Literature", "question": "Who wrote 'Romeo and Juliet'?", 
                 "answers": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"], 
                 "correct": "B", "id": "lit_1_1"},
                
                {"theme": "Sports", "question": "How many players are on a basketball team on the court at one time?", 
                 "answers": ["A) 4", "B) 5", "C) 6", "D) 7"], 
                 "correct": "B", "id": "sport_1_1"},
                
                {"theme": "Geography", "question": "What is the capital of France?", 
                 "answers": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"], 
                 "correct": "C", "id": "geo_1_1"},
                
                {"theme": "Science", "question": "What gas do plants absorb from the atmosphere?", 
                 "answers": ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"], 
                 "correct": "C", "id": "sci_1_1"},
                
                {"theme": "History", "question": "In which year did World War II end?", 
                 "answers": ["A) 1944", "B) 1945", "C) 1946", "D) 1947"], 
                 "correct": "B", "id": "hist_1_1"}
            ],
            
            2: [
                {"theme": "Literature", "question": "Which novel begins with 'Call me Ishmael'?", 
                 "answers": ["A) Moby Dick", "B) The Great Gatsby", "C) Pride and Prejudice", "D) 1984"], 
                 "correct": "A", "id": "lit_2_1"},
                
                {"theme": "Sports", "question": "Which country has won the most FIFA World Cups?", 
                 "answers": ["A) Germany", "B) Argentina", "C) Italy", "D) Brazil"], 
                 "correct": "D", "id": "sport_2_1"},
                
                {"theme": "Geography", "question": "Which is the longest river in the world?", 
                 "answers": ["A) Amazon", "B) Nile", "C) Mississippi", "D) Yangtze"], 
                 "correct": "B", "id": "geo_2_1"},
                
                {"theme": "Science", "question": "What is the chemical symbol for gold?", 
                 "answers": ["A) Go", "B) Gd", "C) Au", "D) Ag"], 
                 "correct": "C", "id": "sci_2_1"},
                
                {"theme": "History", "question": "Who was the first person to walk on the moon?", 
                 "answers": ["A) Buzz Aldrin", "B) Neil Armstrong", "C) John Glenn", "D) Alan Shepard"], 
                 "correct": "B", "id": "hist_2_1"}
            ],
            
            3: [
                {"theme": "Literature", "question": "Who wrote 'One Hundred Years of Solitude'?", 
                 "answers": ["A) Pablo Neruda", "B) Gabriel García Márquez", "C) Mario Vargas Llosa", "D) Jorge Luis Borges"], 
                 "correct": "B", "id": "lit_3_1"},
                
                {"theme": "Sports", "question": "In tennis, what does 'love' mean?", 
                 "answers": ["A) A perfect shot", "B) Zero points", "C) Match point", "D) A tie"], 
                 "correct": "B", "id": "sport_3_1"},
                
                {"theme": "Geography", "question": "Which African country was never colonized?", 
                 "answers": ["A) Kenya", "B) Nigeria", "C) Ethiopia", "D) Ghana"], 
                 "correct": "C", "id": "geo_3_1"},
                
                {"theme": "Science", "question": "What is the hardest natural substance on Earth?", 
                 "answers": ["A) Quartz", "B) Diamond", "C) Granite", "D) Iron"], 
                 "correct": "B", "id": "sci_3_1"},
                
                {"theme": "History", "question": "The Berlin Wall fell in which year?", 
                 "answers": ["A) 1987", "B) 1988", "C) 1989", "D) 1990"], 
                 "correct": "C", "id": "hist_3_1"}
            ],
            
            # Medium questions (4-8)
            4: [
                {"theme": "Literature", "question": "Which Shakespeare play features the character Iago?", 
                 "answers": ["A) Hamlet", "B) Macbeth", "C) Othello", "D) King Lear"], 
                 "correct": "C", "id": "lit_4_1"},
                
                {"theme": "Sports", "question": "What is the maximum score possible in ten-pin bowling?", 
                 "answers": ["A) 200", "B) 250", "C) 300", "D) 350"], 
                 "correct": "C", "id": "sport_4_1"},
                
                {"theme": "Geography", "question": "Which country has the most time zones?", 
                 "answers": ["A) Russia", "B) USA", "C) China", "D) Canada"], 
                 "correct": "A", "id": "geo_4_1"},
                
                {"theme": "Science", "question": "What is the most abundant gas in Earth's atmosphere?", 
                 "answers": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Argon"], 
                 "correct": "C", "id": "sci_4_1"},
                
                {"theme": "History", "question": "Which ancient wonder of the world was located in Alexandria?", 
                 "answers": ["A) Hanging Gardens", "B) Colossus of Rhodes", "C) Lighthouse of Alexandria", "D) Statue of Zeus"], 
                 "correct": "C", "id": "hist_4_1"}
            ],
            
            5: [
                {"theme": "Literature", "question": "Who wrote 'The Picture of Dorian Gray'?", 
                 "answers": ["A) Oscar Wilde", "B) Bram Stoker", "C) Arthur Conan Doyle", "D) H.G. Wells"], 
                 "correct": "A", "id": "lit_5_1"},
                
                {"theme": "Sports", "question": "Which Formula 1 driver has won the most championships?", 
                 "answers": ["A) Ayrton Senna", "B) Michael Schumacher", "C) Lewis Hamilton", "D) Sebastian Vettel"], 
                 "correct": "B", "id": "sport_5_1"},
                
                {"theme": "Geography", "question": "What is the smallest country in the world?", 
                 "answers": ["A) Monaco", "B) San Marino", "C) Vatican City", "D) Liechtenstein"], 
                 "correct": "C", "id": "geo_5_1"},
                
                {"theme": "Science", "question": "What particle is known as the 'God particle'?", 
                 "answers": ["A) Electron", "B) Proton", "C) Neutron", "D) Higgs boson"], 
                 "correct": "D", "id": "sci_5_1"},
                
                {"theme": "History", "question": "Which empire was ruled by Justinian I?", 
                 "answers": ["A) Roman Empire", "B) Byzantine Empire", "C) Ottoman Empire", "D) Persian Empire"], 
                 "correct": "B", "id": "hist_5_1"}
            ],
            
            # Hard questions (6-10)
            6: [
                {"theme": "Literature", "question": "In which James Joyce novel does Leopold Bloom appear?", 
                 "answers": ["A) Dubliners", "B) A Portrait of the Artist", "C) Ulysses", "D) Finnegans Wake"], 
                 "correct": "C", "id": "lit_6_1"},
                
                {"theme": "Sports", "question": "In golf, what is an albatross?", 
                 "answers": ["A) Two under par", "B) Three under par", "C) Four under par", "D) A hole-in-one"], 
                 "correct": "B", "id": "sport_6_1"},
                
                {"theme": "Geography", "question": "Which strait separates Europe and Africa?", 
                 "answers": ["A) Strait of Hormuz", "B) Strait of Gibraltar", "C) Bosphorus Strait", "D) Strait of Malacca"], 
                 "correct": "B", "id": "geo_6_1"},
                
                {"theme": "Science", "question": "What is the name of the theoretical boundary around a black hole?", 
                 "answers": ["A) Photon sphere", "B) Schwarzschild radius", "C) Event horizon", "D) Singularity"], 
                 "correct": "C", "id": "sci_6_1"},
                
                {"theme": "History", "question": "The Treaty of Westphalia ended which war?", 
                 "answers": ["A) Hundred Years' War", "B) Thirty Years' War", "C) Seven Years' War", "D) War of Spanish Succession"], 
                 "correct": "B", "id": "hist_6_1"}
            ],
            
            # Very Hard questions (11-15)
            11: [
                {"theme": "Literature", "question": "Who wrote 'The Master and Margarita'?", 
                 "answers": ["A) Leo Tolstoy", "B) Fyodor Dostoevsky", "C) Mikhail Bulgakov", "D) Anton Chekhov"], 
                 "correct": "C", "id": "lit_11_1"},
                
                {"theme": "Sports", "question": "Which horse won the Triple Crown in 1973?", 
                 "answers": ["A) Seattle Slew", "B) Affirmed", "C) Citation", "D) Secretariat"], 
                 "correct": "D", "id": "sport_11_1"},
                
                {"theme": "Geography", "question": "Which is the highest unclimbed mountain in the world?", 
                 "answers": ["A) Gangkhar Puensum", "B) Muchu Chhish", "C) Kabru", "D) Labuche Kang"], 
                 "correct": "A", "id": "geo_11_1"},
                
                {"theme": "Science", "question": "What is the name of the effect where time dilates due to gravity?", 
                 "answers": ["A) Doppler effect", "B) Gravitational time dilation", "C) Hawking radiation", "D) Quantum entanglement"], 
                 "correct": "B", "id": "sci_11_1"},
                
                {"theme": "History", "question": "Who was the last Byzantine Emperor?", 
                 "answers": ["A) John VIII Palaiologos", "B) Constantine XI Palaiologos", "C) Manuel II Palaiologos", "D) John VII Palaiologos"], 
                 "correct": "B", "id": "hist_11_1"}
            ]
        }

    def display_title(self):
        print("\n" + "="*60)
        print("🎯 WHO WANTS TO BE A MILLIONAIRE? 🎯")
        print("="*60)
        print("Themes: Literature 📚 | Sports ⚽ | Geography 🌍 | Science 🧪 | History 🏛️")
        print("="*60 + "\n")

    def display_money_ladder(self):
        print("\n💰 MONEY LADDER:")
        print("-" * 20)
        for i, amount in enumerate(reversed(self.money_levels)):
            if i == len(self.money_levels) - 1 - self.current_question:
                print(f"► ${amount:,}")
            else:
                print(f"  ${amount:,}")
        print("-" * 20)

    def display_lifelines(self):
        print("\n🆘 LIFELINES AVAILABLE:")
        for lifeline, available in self.lifelines.items():
            status = "✅" if available else "❌"
            print(f"{status} {lifeline}")

    def dramatic_pause(self, text="", duration=2):
        """Add dramatic pauses and music cues for atmosphere"""
        if text:
            print(f"\n🎵 {text} 🎵")
        time.sleep(duration)

    def checkpoint_message(self, level):
        """Display checkpoint messages with dramatic flair"""
        if level == 5:
            print("\n" + "🌟" * 60)
            print("🎊 CHECKPOINT REACHED! 🎊")
            print("💪 You've secured $1,000!")
            print("🛡️ This is your SAFE HAVEN - you cannot fall below this amount!")
            print("🤔 You can walk away now with your guaranteed $1,000...")
            print("🚀 ...OR continue your journey toward MILLIONAIRE STATUS!")
            print("🌟" * 60)
            self.dramatic_pause("*Triumphant checkpoint music plays*", 3)
            
        elif level == 10:
            print("\n" + "⭐" * 60)
            print("🔥 MAJOR CHECKPOINT ACHIEVED! 🔥")
            print("💎 You've secured $32,000!")
            print("🏰 Another SAFE HAVEN - you're guaranteed this amount!")
            print("🎯 Only 5 questions stand between you and $1 MILLION!")
            print("⚖️ The questions get MUCH harder from here...")
            print("🤑 Will you risk it all for the ultimate prize?")
            print("⭐" * 60)
            self.dramatic_pause("*Epic orchestral music intensifies*", 3)

    def use_lifeline(self, q_data):
        print("\nWhich lifeline would you like to use?")
        available_lifelines = [k for k, v in self.lifelines.items() if v]
        
        if not available_lifelines:
            print("No lifelines available!")
            return False
        
        for i, lifeline in enumerate(available_lifelines, 1):
            print(f"{i}. {lifeline}")
        print(f"{len(available_lifelines) + 1}. Cancel")
        
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == len(available_lifelines) + 1:
                return False
            
            selected_lifeline = available_lifelines[choice - 1]
            self.lifelines[selected_lifeline] = False
            
            self.dramatic_pause("*Lifeline activation sound*", 1)
            
            if selected_lifeline == "50/50":
                self.fifty_fifty(q_data)
            elif selected_lifeline == "Phone a Friend":
                self.phone_friend(q_data)
            elif selected_lifeline == "Ask the Audience":
                self.ask_audience(q_data)
            
            return True
            
        except (ValueError, IndexError):
            print("Invalid choice!")
            return False

    def fifty_fifty(self, q_data):
        correct_answer = q_data["correct"]
        answers = q_data["answers"].copy()
        
        # Remove two wrong answers
        wrong_answers = [ans for ans in answers if not ans.startswith(correct_answer)]
        random.shuffle(wrong_answers)
        
        for _ in range(2):
            if wrong_answers:
                answers.remove(wrong_answers.pop())
        
        print("\n🔄 50/50 LIFELINE ACTIVATED!")
        self.dramatic_pause("*Computer processing sounds*", 2)
        print("Two wrong answers have been eliminated:")
        for ans in answers:
            print(ans)

    def phone_friend(self, q_data):
        friends = ["Sarah the Teacher", "Mike the Sports Fan", "Dr. Johnson", "Professor Smith", "Alex the Trivia Master"]
        friend = random.choice(friends)
        
        # Friend has varying accuracy based on question difficulty
        accuracy = 0.9 - (self.current_question * 0.05)
        
        if random.random() < accuracy:
            suggestion = q_data["correct"]
        else:
            wrong_options = ["A", "B", "C", "D"]
            wrong_options.remove(q_data["correct"])
            suggestion = random.choice(wrong_options)
        
        confidence = random.randint(60, 95)
        
        print(f"\n📞 PHONE A FRIEND LIFELINE ACTIVATED!")
        self.dramatic_pause("*Dialing sounds*", 2)
        print(f"Calling {friend}...")
        self.dramatic_pause("*Phone ringing*", 2)
        print(f"\n{friend}: Hello! Oh wow, you're on the show!")
        time.sleep(1)
        print(f"{friend}: Let me think... I'm {confidence}% confident the answer is {suggestion}.")
        print(f"{friend}: Good luck! You've got this!")
        self.dramatic_pause("*Encouraging background music*", 1)

    def ask_audience(self, q_data):
        print("\n👥 ASK THE AUDIENCE LIFELINE ACTIVATED!")
        self.dramatic_pause("*Audience cheering*", 2)
        print("The audience is voting now...")
        self.dramatic_pause("*Voting music plays*", 3)
        
        # Generate audience percentages (correct answer gets higher percentage for easier questions)
        if self.current_question < 5:
            correct_percent = random.randint(60, 85)
        else:
            correct_percent = random.randint(45, 70)
        
        remaining = 100 - correct_percent
        other_percents = []
        
        for i in range(3):
            if i == 2:
                other_percents.append(remaining)
            else:
                percent = random.randint(0, remaining // 2)
                other_percents.append(percent)
                remaining -= percent
        
        options = ["A", "B", "C", "D"]
        correct_idx = options.index(q_data["correct"])
        
        percentages = [0] * 4
        percentages[correct_idx] = correct_percent
        
        other_idx = 0
        for i in range(4):
            if i != correct_idx:
                percentages[i] = other_percents[other_idx]
                other_idx += 1
        
        print("\n📊 AUDIENCE RESULTS:")
        for i, option in enumerate(options):
            print(f"{option}: {'█' * (percentages[i] // 5)} {percentages[i]}%")

    def get_unique_question(self, level):
        """Get a question that hasn't been used yet"""
        questions_for_level = []
        
        # Collect questions from appropriate difficulty ranges
        if level <= 5:
            for q_level in range(1, min(level + 1, 4)):
                questions_for_level.extend(self.questions.get(q_level, []))
        elif level <= 10:
            for q_level in range(4, 7):
                questions_for_level.extend(self.questions.get(q_level, []))
        else:
            questions_for_level.extend(self.questions.get(11, []))
        
        # Filter out used questions
        available_questions = [q for q in questions_for_level if q["id"] not in self.used_questions]
        
        # If all questions are used, reset and allow repeats (shouldn't happen in normal gameplay)
        if not available_questions:
            available_questions = questions_for_level
            self.used_questions.clear()
        
        selected_question = random.choice(available_questions)
        self.used_questions.add(selected_question["id"])
        
        return selected_question

    def ask_question(self, level):
        q_data = self.get_unique_question(level)
        
        # Add dramatic build-up based on question level
        if level <= 5:
            self.dramatic_pause("*Gentle background music*", 1)
        elif level <= 10:
            self.dramatic_pause("*Tension building music*", 2)
        else:
            self.dramatic_pause("*Intense, dramatic music*", 3)
            print("⚡ DANGER ZONE! One wrong answer and you could lose everything! ⚡")
        
        print(f"\n🎲 Question {level} - Theme: {q_data['theme']}")
        print(f"💵 Playing for: ${self.money_levels[level-1]:,}")
        
        # Add extra drama for milestone questions
        if level in [5, 10, 15]:
            print("🎯 MILESTONE QUESTION! 🎯")
            
        print("\n" + q_data["question"])
        print()
        
        for answer in q_data["answers"]:
            print(answer)
        
        # Store the correct answer for later reference
        self.last_correct_answer = q_data["correct"]
        self.last_question_answers = q_data["answers"]
        
        while True:
            print(f"\nYour answer (A/B/C/D), use Lifeline (L), or Walk Away (W): ", end="")
            user_input = input().upper().strip()
            
            if user_input == "W":
                return "walk"
            elif user_input == "L":
                if not self.use_lifeline(q_data):
                    continue
                print("\nNow, what's your final answer? (A/B/C/D): ", end="")
                user_input = input().upper().strip()
            
            if user_input in ["A", "B", "C", "D"]:
                # Add dramatic pause before revealing answer
                print(f"\nYou've chosen {user_input}...")
                if level <= 5:
                    self.dramatic_pause("*Gentle suspense music*", 2)
                elif level <= 10:
                    self.dramatic_pause("*Building tension music*", 3)
                else:
                    self.dramatic_pause("*Heart-pounding suspense music*", 4)
                
                print("Is that your FINAL ANSWER?")
                confirm = input("(Y/N): ").upper().strip()
                if confirm == "Y":
                    return user_input == q_data["correct"]
                else:
                    print("Let's try again...")
                    continue
            else:
                print("Please enter A, B, C, D, L, or W")

    def get_correct_answer_text(self):
        """Get the text of the correct answer"""
        for answer in self.last_question_answers:
            if answer.startswith(self.last_correct_answer):
                return answer
        return f"Option {self.last_correct_answer}"

    def play_game(self):
        self.display_title()
        
        print("🎬 Welcome to Who Wants to Be a Millionaire! 🎬")
        print("🎯 Answer 15 questions correctly to win $1,000,000!")
        print("🆘 You have three lifelines: 50/50, Phone a Friend, and Ask the Audience")
        print("🚶 You can walk away at any time with your current winnings.")
        print("🛡️ Safe havens at $1,000 (Question 5) and $32,000 (Question 10)\n")
        
        self.dramatic_pause("*Opening theme music plays*", 3)
        input("Press Enter to start your journey to become a MILLIONAIRE...")
        
        for level in range(1, 16):
            self.current_question = level - 1
            
            # Show checkpoint messages at safe havens
            if level in [5, 10] and level > 1:
                self.checkpoint_message(level)
                choice = input("\n🤔 Do you want to continue? (Y/N): ").upper().strip()
                if choice == "N":
                    self.current_winnings = self.money_levels[level-2]
                    print(f"\n🚶 You decided to walk away with ${self.current_winnings:,}!")
                    print("💰 A wise and profitable decision!")
                    return
            
            self.display_money_ladder()
            self.display_lifelines()
            
            result = self.ask_question(level)
            
            if result == "walk":
                self.current_winnings = self.money_levels[level-2] if level > 1 else 0
                print(f"\n🚶 You decided to walk away with ${self.current_winnings:,}!")
                print("💼 Sometimes the smart move is knowing when to quit!")
                self.dramatic_pause("*Thoughtful exit music*", 2)
                return
            elif result:
                self.current_winnings = self.money_levels[level-1]
                
                # Dramatic correct answer celebration
                self.dramatic_pause("*Victory fanfare*", 2)
                print(f"\n🎉 CORRECT! You've won ${self.current_winnings:,}! 🎉")
                
                if level == 15:
                    print("\n" + "🏆" * 60)
                    print("🎊 CONGRATULATIONS! YOU'RE A MILLIONAIRE! 🎊")
                    print("💰 You've won $1,000,000! 💰")
                    print("🌟 You've achieved the ultimate prize! 🌟")
                    print("👑 Welcome to the millionaire's club! 👑")
                    print("🏆" * 60)
                    self.dramatic_pause("*Epic victory celebration music*", 5)
                    return
                
                # Safe havens celebration
                if level in [5, 10]:
                    print(f"🛡️ You've reached a SAFE HAVEN! You're guaranteed ${self.current_winnings:,}! 🛡️")
                
                self.dramatic_pause("*Celebratory music continues*", 2)
                input("\nPress Enter for the next question...")
            else:
                # Wrong answer - determine winnings based on safe havens
                if level <= 5:
                    final_winnings = 0
                elif level <= 10:
                    final_winnings = 1000  # Safe haven at question 5
                else:
                    final_winnings = 32000  # Safe haven at question 10
                
                self.dramatic_pause("*Dramatic failure music*", 3)
                print(f"\n❌ WRONG ANSWER! ❌")
                print(f"💔 The correct answer was: {self.get_correct_answer_text()}")
                print(f"📉 You leave with ${final_winnings:,}.")
                
                if final_winnings > 0:
                    print(f"🛡️ At least you had a safe haven to fall back on!")
                else:
                    print("💸 Unfortunately, you leave empty-handed...")
                
                print("🎭 Thanks for playing!")
                self.dramatic_pause("*Consolation music*", 3)
                return

def main():
    while True:
        game = MillionaireGame()  # Reset game for each playthrough
        game.play_game()
        
        print("\n" + "="*50)
        play_again = input("🎮 Would you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print("\n🎬 Thanks for playing Who Wants to Be a Millionaire! 🎬")
            print("💫 Come back anytime to test your knowledge! 💫")
            break

if __name__ == "__main__":
    main()
