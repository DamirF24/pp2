thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


#Duplicate values will overwrite existing values

thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict2)