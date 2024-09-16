Exercise 1: What are the "max_bright" and "min_bright" values you found?
    max_bright = 320
    min_bright = 848

Exercise 2: We decided to play a snippet of the main loading song from Pacman. We found sheet music as well as a way to translate individual notes into frequencies that the speaker can play. 

Exercise 3: 
    data["minimum_response_time"] = min(t_good)
    data["maximum_response_time"] = max(t_good)
    data["average_response_time"] = sum(t_good) / len(t_good)
    data["score"] = (len(t_good) / len(t))
After 10 clicks our program will send a POST request to firebase, this will upload the response time data to the firebase database. This is only made possible through the connection of the Pico W to the internet at the start of the game.
