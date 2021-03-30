# genderize() gendert Input
# WIP: Gibt String genau gleich wieder.
import pandas as pd
import os
import spacy

def genderize(text_input):
	gender_dict = pd.read_csv("gender_me_app/gender_dict.csv")




	nlp = spacy.load("de_core_news_md")
	doc = nlp("Die Studenten wohnen im Studentenwohnheim.")

	for token in doc:
		print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)

	print("--------------------")
	
	ungendered_text = text_input.split(" ")
	gendered_text = []

	for i, word in enumerate(ungendered_text):
		translation = gender_dict[gender_dict["ungendered"] == word]
		if not translation.empty:
			print(translation["gendered"])
			gendered_word = translation.iloc[0,1].split(";")[0]
			print(gendered_word)
			
			if i >= 1:
				if ungendered_text[i-1].lower() == "die":
					gendered_word = gendered_word + "n"
			gendered_text.append(gendered_word)
		else:
			gendered_text.append(word)


	gendered_str = " ".join(gendered_text)
	return gendered_str

if __name__ == '__main__':
	print(genderize("Die Arbeiter wohnen im Studentenwohnheim."))
