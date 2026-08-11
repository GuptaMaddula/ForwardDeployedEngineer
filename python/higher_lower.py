import random


data=[

    {
        'name': 'Instagram',
        'followers': 346000000,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'followers': 215000000,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'followers': 183000000,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'followers': 181000000,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'followers': 174000000,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'followers': 172000000,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'followers': 167000000,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'followers': 149000000,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Beyoncé',
        'followers': 145000000,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Neymar',
        'followers': 138000000,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'National Geographic',
        'followers': 135000000,
        'description': 'Magazine',
        'country': 'United States'
    },
    {
        'name': 'Justin Bieber',
        'followers': 133000000,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Taylor Swift',
        'followers': 131000000,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kendall Jenner',
        'followers': 127000000,
        'description': 'Reality TV personality and Model',
        'country': 'United States'
    },
    {
        'name': 'Jennifer Lopez',
        'followers': 119000000,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Nicki Minaj',
        'followers': 113000000,
        'description': 'Musician',
        'country': 'Trinidad and Tobago'
    },
    {
        'name': 'Nike',
        'followers': 109000000,
        'description': 'Sportswear multinational',
        'country': 'United States'
    },
    {
        'name': 'Khloé Kardashian',
        'followers': 108000000,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Miley Cyrus',
        'followers': 107000000,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': "Katy Perry",
        'followers': 94.5,
        'description': "Musician",
        'country': "United States"
    }
]
score=0
continue_game=True
print("Welcome to the Higher Lower Game!")
print("You will be given two Instagram accounts, and you have to guess which one has more followers.")
random_index_A=0
while continue_game:
    print(f"Compare A: {data[random_index_A]['name']}, a {data[random_index_A]['description']} from {data[random_index_A]['country']}.")
    random_index_B=random.randint(1,len(data)-1)
    print(f"Against B: {data[random_index_B]['name']}, a {data[random_index_B]['description']} from {data[random_index_B]['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if data[random_index_A]['followers'] > data[random_index_B]['followers']:
        correct_answer = 'A'
    else:
        correct_answer = 'B'

    if choice == correct_answer:
        print("You are right!")
        score+=1
        print(f"******************Current score: {score}********************")
        random_index_A=random_index_B
    else:
        print("Sorry, that's wrong.End of the game.")
        print(f"*********************Final score: {score}********************")
        continue_game=False
