f=open("poem.txt")
content=f.read()
if("Ankit" in content):
    print("Ankit is present in the content")
else :
    print("Not present")
f.close()