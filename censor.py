#!/usr/bin/python3
# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()
word = "learning algorithms"
p_t = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censor(email, word):
  data = email
  data = data.replace(word, len(word) * 'X')
  print(data)
  return(data)

def censor_list(email, word_list):
  data = email
  for word in word_list:
    data = data.replace(word, len(word) * 'X')
  return(data)

#censor_list(email_two, p_t)

def negative_censor(email, ls):
  data = censor_list(email, p_t)
  #print(data)
  for word in ls:
    if data.count(word) + data.count(word.title()) + data.count(word.upper()) + data.count(word.lower())>= 2:
      data = data.replace(word, len(word) * 'X')
  return data

#print(negative_censor(email_four, negative_words))

def final_censor(email):
  data = negative_censor(email, negative_words)
  data_split = [i for i in data.split()]
  for i in range(0, len(data_split)):
    if 'X' in data_split[i] and i > 0 and i < len(data_split):
      data_split[i - 1] = data_split[i - 1].replace(data_split[i - 1], len(data_split[i - 1]) * '-')
      data_split[i + 1] = data_split[i + 1].replace(data_split[i + 1], len(data_split[i + 1]) * '+')
      i += 1
    elif 'X' in data_split[i] and i == 0:
        data_split[i + 1] = data_split[i + 1].replace(data_split[i + 1], len(data_split[i + 1]) * '+')
  return ' '.join(data_split)

print("----------")
print(final_censor(email_four))

