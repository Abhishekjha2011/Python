# open
open: file_object=open("file.name.txt","access.mode")
fptr=open("file1.txt","r")
#close
close:file_object.close


#read from start to end:
fp=open("file1.txt","r")
with open("file1.txt","r") as f:
    con=f.read()
    print(con)
#read no. of bytes/char
    fp=open("file1.txt","r")
# real line by line
fp=open("file1.txt","r")
for x in f:
        print(x)
#write into a new file:
        fp=open("file2.txt","w")
        fp.write("text")
        with open("file2.txt","r")as f:
            con=f.read()
            print(con)
#to delete file:
            import os
            os.remove("file.name.txt")
        
fp.close()
