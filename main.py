"""
Enter player name (or "done"): Alice
Enter score for Alice: 95
Enter player name (or "done"): Bob
Enter score for Bob: notanumber
Invalid score. Skipping this entry.
Enter player name (or "done"): Cara
Enter score for Cara: 88
Enter player name (or "done"): done
"""
#store players as a list 
players=[("Sally",95),("Tobi",88),("Sandeep",10),("Zainab",5)]

# setup variable to store summary values
highest_score_player = (None,0)
lowest_score_player = (None,0)
average_score = 0

##pull the scores into a separate list
#declare a new variable to hold a list of scores
#integrate over the player list
#add each score to the new list
player_scores = []
score_total = 0
for player in players:
    player_scores.append(player[1])
    score_total += player[1]
average_score = score_total / len(player_scores)
print(score_total)
print(player_scores)

#find the average
#add all the scores together 
#divide by the number of scores
#set the value of average_score

#output player summary
print("===summary===")
print(f"Players: {len(player)}")
print(f"Highest: {None}") # Sally - 95
print(f"Lowest: {None}") # Zainab - 5
print(f"Average: {average_score}")
