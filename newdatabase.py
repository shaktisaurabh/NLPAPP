import json

class databses:
    def add_new(self,email,name,password):
        with open('dk2.json') as f2:
            db1=json.load(f2)
        if email in db1:
            return 0
        else:
            db1[email]=[name,password]
            with open('dk2.json','w') as f3:
                json.dump(db1,f3)
            return 1
        
    def check(self,email,password):
        with open('dk2.json') as f4:
            db1=json.load(f4)
        if email in db1:
            if db1[email][1]==password:
                return 1
            else:
                return 0
        else:
            return 0 

        