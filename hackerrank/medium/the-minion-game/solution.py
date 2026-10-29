def minion_game(string):
    # your code goes here
    VOCALS = "AEIOU"
    PLAYER1 = "Stuart"
    PLAYER2 = "Kevin"
    score_player1 = 0
    score_player2 = 0
    
    for letter in range(0, len(string)):
        if string[letter] in VOCALS:
            score_player2 += len(string) - letter
        else:
            score_player1 += len(string) - letter
    
    if score_player1 > score_player2:
        print(f"{PLAYER1} {score_player1}")
    elif score_player2 > score_player1:
        print(f"{PLAYER2} {score_player2}")
    else:
        print("Draw")
