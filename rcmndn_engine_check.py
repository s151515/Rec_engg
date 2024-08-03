import random
import sys

# Define a dictionary to store movies (based on moods)
def movies():
        movies = {
            "comedy": ["The Hangover", "21 Jump Street", "welcome", "housefull", "go goa gone", "Hera Pheri", "Munna Bhai M.B.B.S.", "Chup Chup Ke", "Golmaal: Fun Unlimited", "Dhamaal", "Padosan", "Superbad", "The Hangover", "Anchorman: The Legend of Ron Burgundy", "Step Brothers", "Dumb and Dumber", "Bridesmaids"],

            "action": ["The Matrix", "John Wick","Die Hard", "Gladiator", "The Dark Knight", "Inception", "Dhoom", "Dhoom 2", "War", "Singham", "Baaghi", "Ra.One" "Wolverine", "Skyfall", "Black Panther", "Avengers: Endgame", "Guardians of the Galaxy", "Thor: Ragnarok", "Mission: Impossible – Fallout", "The Bourne Identity", "Casino Royale"],

            "adventure": [ "Indiana Jones and the Raiders of the Lost Ark", "Dishoom", "Jumanji", "Pirates of the Caribbean: The Curse of the Black Pearl", "Jurassic Park", "The Lord of the Rings: The Fellowship of the Ring", "The Hobbit: An Unexpected Journey" "Avatar", "The Mummy", "National Treasure", "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe", "The Jungle Book", "Life of Pi", "Harry Potter and the Sorcerer's Stone", "Guardians of the Galaxy", "Star Wars: A New Hope", "Back to the Future", "Ready Player One", "Interstellar", "Madagascar"],

            "drama": ["The Shawshank Redemption", "abigail", "Schindler's List", "Forrest Gump", "The Godfather", "A Beautiful Mind", "The Pursuit of Happyness", "Good Will Hunting", "Fight Club", "The Green Mile", "12 Years a Slave", "The Social Network", "Whiplash", "Moonlight", "Slumdog Millionaire", "Spotlight", "The King's Speech", "Parasite", "Manchester by the Sea", "American Beauty"],

            "thriller": ["Inception", "The Silence of the Lambs", "Joker", "Jurassic Park", "Se7en", "Gone Girl", "Shutter Island", "The Sixth Sense", "The Girl with the Dragon Tattoo", "Prisoners", "No Country for Old Men", "Memento", "Black Swan", "Oldboy", "The Prestige", "Zodiac", "Mulholland Drive", "The Usual Suspects", "A Quiet Place", "Get Out"]
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
                     main()
                    else:
                     print("\n!!!!Press 1 for a different suggestion OR Press 2 if you don't want another suggestion!!!!\n")

            shuffle()

        else:
            print("Sorry, we don't have movie suggestions for ", mood, " yet. Try a different mood!")
            main()

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
                     main()
                    else:
                     print("\n!!!!Press 1 for a different suggestion OR Press 2 if you don't want another suggestion!!!!\n")

            shuffle_food()

        else:
            print("Sorry, we don't have suggestions for ", food_mood, " yet. Try a different taste!")
            main()


###########

def activities():
        activities = {
            "outdoor": ["Go for a walk","Have a picnic","Play badminton", "Ride a bike","Go for a run","Play frisbee","Visit a park","Sit in a cafe outdoors", "Fly a kite","Go for a swim","Play with a street dog","Gardening","Yoga in the park"],

            "indoor": ["Read a book", "Watch a movie or TV series", "Play video games", "Listen to music", "Cook or bake", "Learn a new skill", "Do a puzzle", "Play board games", "Meditate", "Write in a journal", "Organize your space", "Listen to podcasts", "Play with pets", "Try a new recipe"],

            "learning": ["Online course", "Coding tutorial", "Learn a new language", "Read a book", "Write a blog", "Start a podcast", "Take an online quiz", "Follow a YouTube tutorial", "Practice public speaking"],

            "wellness": ["Meditate", "Yoga", "Deep breathing", "Stretching", "Take a bath", "Listen to calming music", "Spend time in nature", "Journaling", "Spend time with loved ones", "Get enough sleep", "Practice mindfulness", "Take a break from screens"],
              }
        # Get user's mood
        activity_mood = input("What kind of activity do u feel like doing(Outdoor, Indoor, Learning, Wellness)? ").lower()
        # Check if user's mood is a valid key in the dictionary
        if activity_mood in activities:
            # Choose
            random_act = random.choice(activities[activity_mood])
            print("\nHere's a", activity_mood, "activity item for you: ", random_act)

            def shuffle_act():  
                while True: # 'while' creates an infinite loop, until the break condition is met..
                    res = int(input("\nDo you want a different suggestion? \nPress 1 for a different suggestion\nPress 2 if this suggestion is good \n"))
                    if res == 1:
                        random_act = random.choice(activities[activity_mood])
                        print("Here is another suggestion:",random_act) 
                    elif res == 2:
                     print ("Enjoy!!")
                     main()
                    else:
                     print("\n!!!!Press 1 for a different suggestion OR Press 2 if you don't want another suggestion!!!!\n")

            shuffle_act()

        else:
            print("Sorry, we don't have suggestions for ", activity_mood, " yet. Try a different activity!")
            main()


def TV_shows():
    shows = {
              "comedy": ["The Office", "Parks and Recreation", "Brooklyn Nine-Nine", "Friends", "The Marvelous Mrs. Maisel", "Sarabhai vs Sarabhai", "F.I.R.", "Taarak Mehta Ka Ooltah Chashmah", "The Kapil Sharma Show"],

            "action": ["24", "Arrow", "Daredevil", "The Punisher", "Jack Ryan", "Powder", "24 (Indian TV series)", "Aarya", "Special OPS", "The Family Man"],

            "adventure": ["Game of Thrones", "Stranger Things", "The Mandalorian", "The Witcher", "Lost", "Khatron Ke Khiladi", "Discovery of India", "Everest"],

            "drama": ["Breaking Bad", "Mad Men", "The Crown", "This Is Us", "The Handmaid's Tale", 
        "Sacred Games", "Made in Heaven", "Paatal Lok", "Mirzapur"],

            "thriller": ["Mindhunter", "True Detective", "Black Mirror", "Dexter", "You", 
        "Sacred Games", "Breathe", "Mirzapur", "Criminal Justice"]
             }
     # Get user's mood
    show_mood = input("What do u feel like watching(comedy, action, adventure, drama, thriller)? ").lower()

    if show_mood in shows:
            # Choose  
            random_show = random.choice(shows[show_mood])
            print("\nHere's a", show_mood, "movie suggestion for you: ",random_show)

            def shuffle():  
                while True: 
                    res = int(input("\nDo you want a different suggestion? \nPress 1 for a different suggestion\nPress 2 if this suggestion is good \n"))
                    if res == 1:
                        random_show = random.choice(shows[show_mood])
                        print("Here is another suggestion:",random_show) 
                    elif res == 2:
                     print ("Enjoy!!")
                     main()
                    else:
                     print("\n!!!!Press 1 for a different suggestion OR Press 2 if you don't want another suggestion!!!!\n")

            shuffle()

    else:
            print("Sorry, we don't have TV show suggestions for ", show_mood, " yet. Try a different mood!")
            main()
    

def main():
    what = int(input("\nWhat do you need a suggestion for? \n\nPress 1 for movies\nPress 2 for food items\nPress 3 for entertaining activities\nPress 4 for TV shows\nPress 0 to exit\n"))

    if what == 1:
            movies()
    elif what == 2:
            food()
    elif what == 3:
            activities()
    elif what == 4:
            TV_shows()
    elif what == 0:
            print("Thankyou!")
            sys.exit()
            
    else:
         print("\n!!Choose a number between 1-4!!\n")
         main()

main()