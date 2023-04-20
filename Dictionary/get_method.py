# get method is used if we want that if the value does'nt exist the dict will return None instead of throwing error
dict = {
    "Waqar": "is Good",
    3: "is bad"
}
print(dict.get("Waqars"))  # dict[waqars] will throw error in the program
