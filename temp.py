def main():
  import sys
  print("please select one of the options below and answer questions as accurately as possible to ensure the best results")
menu=input("What subject do you prefer:computerscience or media")
if menu == "computerscience":
  csone=input("which of the following do you enjoy more?hardware or software")
  if csone == "software":
    cstwo=input("Would you rather do:data,programming,cyber security")
    if cstwo == "cyber security":
      print("You have the choice of being a security analyst,security enginerer or cryptographer")
    elif cstwo == "programming":
      print("You have the choice of being a software application developer or web developer")
    else:
      print("You have the choice of being a data architect,data scientist or a data engineerer")
  else:
    print("Your future career is a hardware engineer!")
elif menu == "media":
  mdone=input("Which of the following suits you the most:digital animation,graphic design or game design")
  if mdone == "digital animation":
    print ("You have chosen digital animation so your destined career is to be an animation technical director or videographer or a 3d modeler")
  elif mdone == "graphic designer":
    print("Your destined career is a graphic designer- creating visual concepts, by hand or using computer software, to communicate ideas that inspire, inform, or captivate consumers.")
  else:
    print("You will work as a team to produce games-a game designer.This can be by simply creating 2d/3d characters or creating the  software programme")
else:
  print("please write the answer exactly how it is written in the question")
