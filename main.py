from score_stats import calculative_avg_score
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
average_score = calculate_average_score(players)




#output player summary


