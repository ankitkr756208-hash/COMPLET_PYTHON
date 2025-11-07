def rem(l,word):
    for item in l:
        l.remove(word)
        return l
    
l=["ankit","Rohan","Sohan","anand"]
print(rem(l,"ankit"))