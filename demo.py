nouns = ['lion', 'tiger', 'bass', 'cup']

def convert_to_plural(word):
  if word[-1] == "s":
    return word + "es"
  else:
    return word + "s"

plural = []
for noun in nouns:
  plural.append(convert_to_plural(noun))


print(plural)
