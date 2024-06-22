import os

def remove_leading_number(s:str)->str:
    i=0
    for j in range(len(s)):
        if s[j].isdigit():
            i+=1
        else:
            break
    return s[i:]
        

os.makedirs("out",exist_ok=True)
f=open("out/index.md","w",encoding="utf-8")

dirs = [i for i in os.listdir("src") if not os.path.isfile(i) and i not in [".git","out",".github"]]
dirs.sort()
for chapter in dirs:
    f.write("# "+remove_leading_number(chapter)+"\n\n")
    files=os.listdir("src/"+chapter)
    files.sort()
    for file in files:
        f.write("## "+file.replace(".md","")+"\n\n")
        with open("src/"+chapter+"/"+file,"r",encoding="utf-8") as f2:
            f.write(f2.read()) 
            f.write("\n\n")
with open("footer.md") as footer:
    f.write("\n")
    f.write(footer.read())

f.close()