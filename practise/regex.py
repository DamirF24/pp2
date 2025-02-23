import re


text_to_match = "Returns a list containing all matches, all,all,all of worlds, all"
cnt = 0 
pattern = re.findall("all",text_to_match)
  
cnt += len(pattern)



if cnt > 1:
    print(f"Yes, there are {cnt} matches")
elif cnt==1:
    print("only one match")

else :
    print("No match")