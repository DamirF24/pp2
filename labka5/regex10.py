import re


text_to_match = "TheQuickBrownFoxJumpsOverTheLazyDog"

pattern = re.sub(r"(?<!^)([A-Z])",r"_\1",text_to_match)
ffpattern = pattern.lower()

print(ffpattern)