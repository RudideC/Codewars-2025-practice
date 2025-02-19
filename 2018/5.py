name = input()
age = input()
gender = input()
pronoun = "She" if gender == "girl" else "He"
possesive_pronoun = "her" if gender == "girl" else "his"
city = input()
sport = input()
team = input()
job = input()

print(f"{name} is a {age} year-old {gender}. {pronoun} is living with {possesive_pronoun} parents in an apartment in the centre of {city}, where {pronoun.lower()} hangs out with {possesive_pronoun} friends. Moreover, in {possesive_pronoun} free time {pronoun.lower()} plays {sport} in a team called {team}. {name} would like to pursue a career in {job} when {pronoun.lower()} is older, that's why {pronoun.lower()} is studying hard.")