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
player=[("Sally",95),("Tobi",88),("Sandeep",10),("Zainab",5)]


#output player summary
print("===summary===")
print(f"Players: {len(player)}")
print(f"Highest: {None}") # Sally - 95
print(f"Lowest: {None}") # Zainab - 5
print(f"Average: {None}")
