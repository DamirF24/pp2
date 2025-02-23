import re


text_to_match = "TheQuickBrownFoxJumpsOverTheLazy"
pattern = re.sub(r"(?<!^)([A-Z])",r" \1",text_to_match)
finalpattern = re.split(r"\s",pattern)

print(finalpattern)