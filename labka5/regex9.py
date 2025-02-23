import re

text_to_match = "TheQuickBrownFoxJumpsOverTheLazyDog"


pattern = re.sub(r"(?<!^)([A-Z])",r" \1",text_to_match)

print(pattern)



