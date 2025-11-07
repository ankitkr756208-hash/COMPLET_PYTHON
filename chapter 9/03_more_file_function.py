f=open("file.txt")
lines=f.readlines()
while(lines !="" ):
    print(lines)
    line=f.readline()

# # print(lines,type(lines))

f.close()