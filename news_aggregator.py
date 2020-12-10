from newspaper import Article
import nltk
nltk.download('punkt')
Url = input("Enter the url == ")
A = Article(Url,language="en")
A.download()
A.parse()
print("Brief ==",A.text[:150])
print("Title ==",A.title)
print("Top Image ==",A.top_image)
A.nlp()
print("Keyword ==",A.keywords)
