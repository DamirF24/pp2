import re
text_to_match = "the_quick_brown_fox_jumps_over_the_lazy_dog"


pattern = re.sub("_"," ",text_to_match)
finalpattern = pattern.title()
finalfinal = re.sub(r"\s+", "",finalpattern)
print(finalfinal)