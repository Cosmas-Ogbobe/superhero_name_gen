import random

def generate_superhero_name():
    adjectives = ['Amazing', 'Mighty', 'Incredible', 'Radiant', 'Dynamic', 'Fantastic', 'Epic', 'Mysterious', 'Supreme']
    nouns = ['Phoenix', 'Spectre', 'Guardian', 'Vortex', 'Centurion', 'Enigma', 'Blaze', 'Thunder', 'Pinnacle']

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    superhero_name = f"{adjective} {noun}"
    return superhero_name

# Generate and print a superhero name
hero_name = generate_superhero_name()
print(f"Your superhero name is: {hero_name}")
