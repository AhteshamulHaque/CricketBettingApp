# Types of conditions returned by _get_game_condition()
game_condition = [ # it's always an single dictionary
    { 'inning': 1, 'over': 2, 'wicket': 2, 'krate': 0.3, 'lrate': 0.6, 'team': 'INDIA'},
    { 'inning': 2, 'over': 2, 'wicket': 2, 'krate': 0, 'lrate': 0.95, 'team': ['AUS', 'INDIA']},
]

# Types of conditions in conditions variable
state_conditions = [
    {'rate': 0.3, 'over': 12, 'inning': 1, 'wicket': 2, type:'k'},
    {'rate': 0.6, 'over': 0, 'inning': 0, 'wicket': 0, type:'l'},
]

# update prev_condition after a condition matches
prev_condition = { 'type': 'k', 'team': 'AUS'}


# Winning Conditions
| First bet | Second bet |   Team    |      Bet      |
|----------------------------------------------------|
|     L     |     K      |   Same    | high then low |
|     K     |     L      |   Same    | low then high |
|     K     |     K      | Different |      any      |

# update position A and position B in memory, do not rely on real data because more
# than 2 policies could be running in the same id. So, it may not be possible to
# differentiate between them simultaneously.