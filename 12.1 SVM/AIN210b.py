#nltk.download('all')
import re
from nltk.corpus import stopwords  #to remove stopwords
from nltk.stem.porter import PorterStemmer  #used for Stemming

def clean_data1(text):
    text = text.lower().strip()
    text = re.sub(r"<br>"," ", text)
    text = re.sub(r"([-?.!,/\"])",r" \1 ", text)
    text = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,']", "", text)
    text = re.sub(r"[ ]+", " ", text)
    text = text.rstrip().strip()
    return text

ps = PorterStemmer()
def clean_data2(text):
    text = text.split()
    new_text = [ps.stem(word) for word in text if word not in stopwords.words('english')]
    new_text = " ".join(new_text)
    return new_text

