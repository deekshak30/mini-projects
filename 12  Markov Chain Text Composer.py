 import markovify
with open(r"C:\Users\bhava\Pictures\corpus.txt") as f:
    text = f.read()
text_model = markovify.Text(text)
for i in range(5):
    print(text_model.make_sentence())
for i in range(3):
    print(text_model.make_short_sentence(200))
