import paralleldots as pd

class ohmyapi:
    def __init__(self):
        pd.set_api_key("SFR5JkA3wK3cXmOHiBzeqmjbW5jAiCbHiwE5QPI0cdM")
    def get_senti(self,text):
        c1=pd.sentiment(text)
        return c1 
    def get_neri(self,text):
        c1=pd.ner(text)
        return c1 
    def get_abuse(self,text):
        c1=pd.abuse(text)
        return c1
