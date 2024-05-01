import nltk
#nltk.download('wordnet')
from nltk.stem import PorterStemmer, WordNetLemmatizer 

from nltk.sentiment import SentimentIntensityAnalyzer
text=""" Welcome you to pragramming knowledge. Lets start with our first tutorial on NLTK. We shall learn the basics of NLTK here."""
demoWords= ["playing","Happiness","going", "go","doing","do","yes", "no", "I", "having", "had", "haved", "coding", "programming","code", "program"]
lemmeatizer= WordNetLemmatizer()
stemmer=  PorterStemmer()
#for word in demoWords:
 #   #left stem right lemmatize
  #  print(stemmer.stem(word),lemmeatizer.lemmatize(word,"v"))
#for word in demoWords:
 #   #word stem lemmatize
  #  print(word, stemmer.stem(word),lemmeatizer.lemmatize(word,"v"))
  
sia=SentimentIntensityAnalyzer()
print(sia.polarity_scores("The Government generally respected the human rights of its citizens; however, there were serious problems in some areas. There were no reports of security forces committing politically motivated killings and no reports of disappearances; however, the military and police reportedly tortured, killed, and raped detainees."))
#print(sia.polarity_scores("Programming is fun"))
#print(sia.polarity_scores("You behaved very bad today"))
#print(sia.polarity_scores("This is not good at all"))