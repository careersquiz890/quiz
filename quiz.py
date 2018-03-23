import json
from pprint import pprint

data = json.load(open('questions.json'))

#pprint(data)
 
def main():
  # print 1st question
  print("please select one of the options below and answer questions as accurately as possible to ensure the best results")
  #print(data[0])

  #text = get_question_text(data[0])

  #menu=input(text)

  #print(menu)

  # based on menu get the id from data[0]["choices"]

  choices = {}
  selId = ""
  # print the next relevant question
  # iterate over data but skip index 0 and then look for id from choice
  for idx, val in enumerate(data):
    if idx > 0 and val["type"] != selId:
      continue

    text = get_question_text(data[idx])

    #print(text)
    menu=input(text)

    if idx == 0:
      selId = val["choices"][menu-1]["id"]  
      print("You selected:" + selId)

    # validate menu


def get_question_text(question):
  text = question["text"] + "\n"
  # iterate data[0].choices
  for idx, val in enumerate(question["choices"]):
    text = text + str(idx + 1) + ". " + val["text"] + "\n"
    #print(idx, val)

  return text

if __name__== "__main__":
  main()
