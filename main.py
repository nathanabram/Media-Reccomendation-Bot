name = input('Hi there. I am a media recommendation bot. \nWha is your name?\n')
print ("\nWelcome, %s." % name)
while True:
  desiredMedia = str(input("Which of the following are you looking for?\n \n\
  1) Music \n\
  2) Podcast \n\
  3) Movie \n\
  4) Game \n\
  5) Book \n\
  6) Article \n\
  ") )
  mediaIndex = 0
  def mediaSwitcher(arg):
    switcher = {
        "Music" : 0,
        "Podcast" : 1,
          "Movie" : 2,
          "Game" : 3,
          "Book" : 4,
          "Article" : 5,
          "1" : 6,
          "2" : 7,
          "3" : 8,
          "4" : 9,
          "5" : 10,
          "6" : 11
    }
    return switcher.get(arg, "Please choose one of the things listed above.")
  def mediaRecs(arg):
      switcher = {
        0 : "\"the last great american dynasty\" by Taylor Swift",
        1 : "The After On Podcast: \"The Medical Potential of Video Games | Adam Gazzaley\"",
        2 : "\"Burn After Reading\" by Ethan & Joel Coen",
        3 : "\"Agar.io\" by Matheus Valadares",
        4 : "\"The Crystal Society\" by Max Harms",
        5 : "\"Life Spirit Distillation\" by Venkatesh Rao"
      }
      return switcher.get(arg)

  mediaIndex = mediaSwitcher(desiredMedia) 
  mediaIndex = mediaIndex % 6 
  reccomendation = mediaRecs(mediaIndex)
  userContinue = input ("Okay %s, I think you should check out %s. \nWant another recommendation? (y/n)" % (name, reccomendation))
  if userContinue == ("y" or "yes" or "Y" or "Yes"):
    continue 
  elif userContinue == ("n" or "no" or "N" or "No"):
    print ("Okay, well thanks for visiting. Enjoy!")
    break
  else:
    break

