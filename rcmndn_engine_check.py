import random

# Define a dictionary to store movies and their moods
def movies():
        movies = {
            "comedy": ["The Hangover", "21 Jump Street", "welcome", "housefull", "go goa gone", "Hera Pheri", "Munna Bhai M.B.B.S.", "Chup Chup Ke", "Golmaal: Fun Unlimited", "Dhamaal", "Padosan", "Superbad", "The Hangover", "Anchorman: The Legend of Ron Burgundy", "Step Brothers", "Dumb and Dumber", "Bridesmaids"],

            "action": ["The Matrix", "John Wick","Die Hard", "Gladiator", "The Dark Knight", "Inception", "Dhoom", "Dhoom 2", "War", "Singham", "Baaghi", "Ra.One" "Wolverine", "Skyfall", "Black Panther", "Avengers: Endgame", "Guardians of the Galaxy", "Thor: Ragnarok", "Mission: Impossible – Fallout", "The Bourne Identity", "Casino Royale"],

            "adventure": [ "Indiana Jones and the Raiders of the Lost Ark", "Dishoom", "Jumanji", "Pirates of the Caribbean: The Curse of the Black Pearl", "Jurassic Park", 
                "The Lord of the Rings: The Fellowship of the Ring", "The Hobbit: An Unexpected Journey", "Avatar", "The Mummy", "National Treasure", 
                "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe", "The Jungle Book", "Life of Pi", "Harry Potter and the Sorcerer's Stone", "Guardians of the Galaxy", 
                "Star Wars: A New Hope", "Back to the Future", "Ready Player One", "Interstellar", "Madagascar"
            ],
            "drama": [
                "The Shawshank Redemption", "abigail", "Schindler's List", "Forrest Gump", "The Godfather", 
                "A Beautiful Mind", "The Pursuit of Happyness", "Good Will Hunting", "Fight Club", "The Green Mile", 
                "12 Years a Slave", "The Social Network", "Whiplash", "Moonlight", "Slumdog Millionaire", 
                "Spotlight", "The King's Speech", "Parasite", "Manchester by the Sea", "American Beauty"
            ],
            "thriller": [
                "Inception", "The Silence of the Lambs", "Joker", "Jurassic Park", "Se7en", 
                "Gone Girl", "Shutter Island", "The Sixth Sense", "The Girl with the Dragon Tattoo", "Prisoners", 
                "No Country for Old Men", "Memento", "Black Swan", "Oldboy", "The Prestige", 
                "Zodiac", "Mulholland Drive", "The Usual Suspects", "A Quiet Place", "Get Out"
            ]
        }

        # Get user's mood
        mood = input("What's your mood today (comedy, action, adventure, drama, thriller)? ").lower()

        # Check if user's mood is a valid key in the dictionary
        if mood in movies:
            # Choose a random movie from the list of movies for that mood
            random_movie = random.choice(movies[mood])
            print("\nHere's a", mood, "movie suggestion for you: ",random_movie)

            def shuffle():  
                while True: # 'while' creates an infinite loop, until the break condition is met..
                    res = int(input("\nDo you want a different suggestion? \nPress 1 for a different suggestion\nPress 2 if this suggestion is good \n"))
                    if res == 1:
                        random_movie = random.choice(movies[mood])
                        print("Here is another suggestion:",random_movie) 
                    elif res == 2:
                     print ("Enjoy!!")
                     break
                    else:
                     print("\n!!!!Press 1 for a different suggestion OR Press 2 if you don't want another suggestion!!!!\n")

            shuffle()

        else:
            print("Sorry, we don't have movie suggestions for ", mood, " yet. Try a different mood!")

###########

def food():
        food = {
            "spicy": ["Chili", "Jalapeno", "Wasabi", "Pepper"],

            "sweet": ["Chocolate", "Ice cream", "Cake", "Candy"],

            "healthy": ["Salad", "Fruits", "Vegetables", "Whole grains", "Nuts"],

            "Savory": ["Pizza", "Pasta", "Burger", "Fries", "Chicken", "Steak"],

            "Bitter": ["Coffee", "Dark chocolate", "Olive oil", "Broccoli", "Spinach"]
              }
        # Get user's mood
        food_mood = input("What do u feel like eating(spicy, sweet, healthy, Savory, Bitter)? ").lower()

        # Check if user's mood is a valid key in the dictionary
        if food_mood in food:
            # Choose
            random_food = random.choice(food[food_mood])
            print("\nHere's a", food_mood, "food item for you: ",random_food)

            def shuffle_food():  
                while True: # 'while' creates an infinite loop, until the break condition is met..
                    res = int(input("\nDo you want a different suggestion? \nPress 1 for a different suggestion\nPress 2 if this suggestion is good \n"))
                    if res == 1:
                        random_food = random.choice(food[food_mood])
                        print("Here is another suggestion:",random_food) 
                    elif res == 2:
                     print ("Enjoy!!")
                     break
                    else:
                     print("\n!!!!Press 1 for a different suggestion OR Press 2 if you don't want another suggestion!!!!\n")

            shuffle_food()

        else:
            print("Sorry, we don't have movie suggestions for ", food_mood, " yet. Try a different mood!")

def TV_shows():
    shows = {
              "": [], 
              "": [],
              "": [],
              "": [],
              "": [],
             }
    
    

def main():
    what = int(input("What do you need a suggestion for? \nPress 1 for movies\nPress 2 for food items\n"))

    if what == 1:
        movies()
    elif what == 2:
        food()
        
    else: 
        print("\n!!Choose a number between 1-2!!\n")
        main()

main()