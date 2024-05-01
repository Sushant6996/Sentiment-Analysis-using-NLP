import nltk 
import matplotlib.pyplot as plt
#nltk.download('punkt')

text=""" Welcome you to pragramming knowledge. Lets start with our first tutorial on NLTK. We shall learn the basics of NLTK here."""
from nltk.tokenize import word_tokenize
words=word_tokenize(text)
#from nltk.tokenize import sent_tokenize
#print(sent_tokenize(text))

from nltk.probability import FreqDist
fd=FreqDist(words)
print(fd.most_common(3))
fd.plot(30,cumulative=False)
plt.show()
 