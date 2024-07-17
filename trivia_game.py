import argparse
import json
import pathlib
import random


class TriviaGamePlayer:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def add_score(self, points):
        self.points += points

    @staticmethod
    def get_highest_score_players(players: list['TriviaGamePlayer']) -> list['TriviaGamePlayer']:
        max_score = max(player.points for player in players)
        return [player for player in players if player.points == max_score]

    def __str__(self) -> str:
        return self.name


def choose_questions_file(file_path):
    content = pathlib.Path(file_path).read_text()
    return json.loads(content)


def ask_question(question):
    print(question['question'])
    for option in ['A', 'B', 'C', 'D']:
        print(f"{option}. {question[option]}")
    return input("Your answer (enter A, B, C, or D): ")


def check_valid_input(user_answer: str):
    return user_answer.upper() in ['A', 'B', 'C', 'D']


def is_player_right(question, user_answer):
    return user_answer.upper() == question['answer']


def shuffle_answer_options(question):
    options = ['A', 'B', 'C', 'D']
    shuffled_options = random.sample(options, len(options))
    shuffled_question = {
        'question': question['question'],
        'answer': shuffled_options[options.index(question['answer'])]
    }
    for old, new in zip(options, shuffled_options):
        shuffled_question[new] = question[old]
    return shuffled_question


def get_available_options(question, guessed_answers):
    return [option for option in ['A', 'B', 'C', 'D'] if option not in guessed_answers]


def main():
    parser = argparse.ArgumentParser(description="Trivia Game.")
    parser.add_argument('--file', type=str, required=True, help='Path to the questions file')
    parser.add_argument('--players', type=int, required=True, help='Number of players')
    parser.add_argument('--rounds', type=int, required=True, help='Number of rounds')
    args = parser.parse_args()

    original_questions = choose_questions_file(args.file)

    players = []
    for i in range(1, args.players + 1):
        player = TriviaGamePlayer(input(f"Enter the name of player number {i}: "))
        players.append(player)
    print(", ".join(player.name for player in players), "Good luck!")

    current_question = 0
    questions = random.sample(original_questions, len(original_questions))
    current_shuffled_question = None
    guessed_answers = set()

    for round_num in range(1, args.rounds + 1):
        print(f"\nRound number {round_num}")
        for player in players:
            if current_question >= len(questions):
                print("No more questions available. Game over.")
                break

            if current_shuffled_question is None:
                current_shuffled_question = shuffle_answer_options(questions[current_question])
                guessed_answers.clear()

            print(f"\n{player.name}, it's your turn.")
            available_options = get_available_options(current_shuffled_question, guessed_answers)

            if not available_options:
                print("All options have been guessed. Moving to the next question.")
                current_question += 1
                current_shuffled_question = None
                continue

            print(current_shuffled_question['question'])
            for option in available_options:
                print(f"{option}. {current_shuffled_question[option]}")

            user_answer = input(f"Your answer (enter {', '.join(available_options)}): ")

            while user_answer.upper() not in available_options:
                user_answer = input(f"Please enter one of these options: {', '.join(available_options)}: ")

            guessed_answers.add(user_answer.upper())

            if is_player_right(current_shuffled_question, user_answer):
                print(f"{player.name}, you got a point!")
                player.add_score(1)
                current_question += 1
                current_shuffled_question = None
                guessed_answers.clear()
            else:
                print(f"Sorry, {player.name}, that's incorrect.")

        if current_question >= len(questions):
            break

    print("\nGame is over")
    winners = TriviaGamePlayer.get_highest_score_players(players)
    print("Final scores:")
    for player in players:
        print(f"{player.name}: {player.points} points")
    print("\nWinner(s):", ", ".join(str(winner) for winner in winners))


if __name__ == "__main__":
    main()
