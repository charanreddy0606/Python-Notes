
'''with open("readwrite","r") as file:
    content =file.read()
    print("original content",content)

    new_content = content.replace("readwrite","new_readwrite")
    print("original content", new_content)

    file.seek(0)
    file.write(new_content)
    file.truncate()'''
# open new data to read the content
with open("new_readwrite","r") as file:
    content =file.read()
# open readwrite to write the new data at end

with open("readwrite","w") as old_file:
    old_file.write(content)

# verify the result by reading old data
with open("readwrite",'r')as old_file:
    print("updated old data content")
    print(old_file.read())
        
