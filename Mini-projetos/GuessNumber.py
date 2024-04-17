import random
while True:
 def play_game():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != number_to_guess:
        guess = int(input("Advinhe um número entre 1 e 10: "))
        attempts += 1

        if guess < number_to_guess:
            print("O número é maior!")
        elif guess > number_to_guess:
            print("O número é menor!")

    print(f"Parabéns! Você acertou o número em {attempts} tentativas.")

 if __name__ == "__main__":
    play_game()
    
 msg = input("Quer jogar de novo? S/N: ")
 if msg != "S":
    print("Obrigado por jogar!")
    break
