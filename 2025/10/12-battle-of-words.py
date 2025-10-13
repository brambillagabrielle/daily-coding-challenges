'''
Given two sentences representing your team and an opposing team, where each word from your team battles the corresponding word from the opposing team, determine which team wins using the following rules:
 - The given sentences will always contain the same number of words.
 - Words are separated by a single space and will only contain letters.
 - The value of each word is the sum of its letters.
 - Letters a to z correspond to the values 1 through 26. For example, a is 1, and z is 26.
 - A capital letter doubles the value of the letter. For example, A is 2, and Z is 52.
 - Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
 - A word wins if its value is greater than the opposing word's value.
 - The team with more winning words is the winner.
Return "We win" if your team is the winner, "We lose" if your team loses, and "Draw" if both teams have the same number of wins.
'''

def battle(our_team, opponent):
    team_1 = our_team.split(" ")
    team_2 = opponent.split(" ")
    
    total_score_team_1 = 0
    total_score_team_2 = 0

    for i in range(len(team_1)):
        score_team_1 = 0
        for l in team_1[i]:
            if l.islower():
                score_team_1 += ord(l)%32
            else:
                score_team_1 += (ord(l)%32) * 2

        score_team_2 = 0
        for l in team_2[i]:
            if l.islower():
                score_team_2 += ord(l)%32
            else:
                score_team_2 += (ord(l)%32) * 2

        if score_team_1 > score_team_2:
            total_score_team_1 += 1
        elif score_team_1 < score_team_2:
            total_score_team_2 += 1

    if total_score_team_1 > total_score_team_2:
        return "We win"
    elif total_score_team_1 < total_score_team_2:
        return "We lose"
    else:
        return "Draw"

print("Success") if battle("hello world", "hello word") == "We win" else print("Failed")
print("Success") if battle("Hello world", "hello world") == "We win" else print("Failed")
print("Success") if battle("lorem ipsum", "kitty ipsum") == "We lose" else print("Failed")
print("Success") if battle("hello world", "world hello") == "Draw" else print("Failed")
print("Success") if battle("git checkout", "git switch") == "We win" else print("Failed")
print("Success") if battle("Cheeseburger with fries", "Cheeseburger with Fries") == "We lose" else print("Failed")
print("Success") if battle("We must never surrender", "Our team must win") == "Draw" else print("Failed")