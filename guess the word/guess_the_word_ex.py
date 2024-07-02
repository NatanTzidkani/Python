import json
import pathlib
import argparse


ENGLISH_LETTERS = 26


class GuessGamePlayer:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def add_score(self, points):
        self.points += points

    @staticmethod
    def get_highest_score_players(players: list['GuessGamePlayer']) -> list['GuessGamePlayer']:
        max_score = max(player.points for player in players)
        return [player for player in players if player.points == max_score]

    def __str__(self) -> str:
        return self.name


def choose_word(file_path, index):
    content = pathlib.Path("output.json").read_text()
    words_list = list(set(json.loads(content)))
    return words_list[index % len(words_list) - 1]


def check_valid_input(letter_guessed, old_letters_guessed):
    return (
            len(letter_guessed) == 1 and
            letter_guessed.isalpha() and
            letter_guessed.lower() not in old_letters_guessed
    )


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    print("X")
    sorted_old_letters_guessed_to_user = sorted(old_letters_guessed, key=str.lower)
    print(" -> ".join(sorted_old_letters_guessed_to_user))
    return False


def show_hidden_word(secret_word, old_letters_guessed):
    return " ".join(
        secret_letter if secret_letter in old_letters_guessed else "_"
        for secret_letter
        in secret_word
    )


def is_all_guessed(secret_word, old_letters_guessed):
    return all(letter in old_letters_guessed for letter in secret_word)


def main():
    # python.exe .\guess_the_word_ex.py --player asdasd --player asdzc
    parser = argparse.ArgumentParser(description="Guess The Word Game.")
    parser.add_argument('--player', type=str, action='append', help='Name of the player')
    args = parser.parse_args()
    players = []
    if args.player:
        print("Inputs received:")
        for player in args.player:
            player = GuessGamePlayer(player)
            players.append(player)
    else:
        print("Welcome to the game !!!!")
        print("Let’s start!")

        num_of_players = int(input("Enter the number of players: "))
        for i in range(1, num_of_players + 1):
            player = GuessGamePlayer(input(f"Enter the name of player number {i}: "))
            players.append(player)
    print(", ".join(player.name for player in players), "Good luck!")

    # choose_word(r"C:\python_ex\self_py\words.txt", 5)
    # secret_word = choose_word(input("Enter file path: "), int(input("Enter index to randomize a word: ")))
    secret_word = "robert"

    old_letters = []
    i = 1
    while i < ENGLISH_LETTERS:
        print(f"Round number {i}")

        for player in players:
            user_input = input(player.name + ", Guess a letter: ")
            user_guess = try_update_letter_guessed(user_input, old_letters)
            while not user_guess:
                user_input = input("Guess a valid letter, only English letters : ")
                user_guess = try_update_letter_guessed(user_input, old_letters)

            if user_input in secret_word:
                points = secret_word.count(user_input)
                print(player.name + f", you got {points} points !")
                player.add_score(points)
                print(show_hidden_word(secret_word, old_letters))

            if is_all_guessed(secret_word, old_letters):
                print("Game is over")
                winners = GuessGamePlayer.get_highest_score_players(players)
                for winner in winners:
                    print(winner, end=", ")
                print("Won the game!")
                exit()
        i += 1


if __name__ == "__main__":
    main()
