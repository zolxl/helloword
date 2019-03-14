class Person:
    def __init__(self, name, lang="golang", website="www.google.com"):
        self.name = name
        self.lang = lang
        self.website = website
        self.email = "zolxl6@gmail.com"

laoqi = Person("LaoQi")     
info = Person("Popye",lang="python",website="https://github.com/zolxl")

print("laoqi.name=",laoqi.name)
print ("info.name=",info.name)
print ("-------")
print ("laoqi.lang=",laoqi.lang)
print ("info.lang=",info.lang)
print ("-------")
print ("laoqi.website=",laoqi.website)
print ("info.website=",info.website)
