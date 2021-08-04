def named_entities(text, language):

  nlp = spacy.load(language)
  doc = nlp(text)

  return [{"text": ent.text,
           "type": ent.label_,
           "start_pos": ent.start_char,
           "end_pos": ent.end_char} for ent in doc.ents]



if __name__ == "__main__":

  text = "Apple is looking at buying U.K. startup for $1 billion"
  language_code = "en"

  print(named_entities(text, language_code))
