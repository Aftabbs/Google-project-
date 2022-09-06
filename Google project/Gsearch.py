from googlesearch import search as s

keywords=input("enter your query")

result=s(keywords,6)

for i in result:
    print(i)
    
