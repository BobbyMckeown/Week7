# TASK1
names = {"John", "Eric", "Terry", "Michael", "Graham", "Terry"}
print(names)
# TASK2
sentence = "this is a sentence containing some letters"
unique_letters = {x for x in sentence}
print(unique_letters)
# TASK3
name = input("Enter your name: ")
if name not in names:
    print("You are NOT listed in the set of known names")

# help(set)
# TASK4
staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
directors = {"Kelly", "Rupert", "Cyril", "Jon"}

staff = staff.union({"Paul", "Mckeown"})
print(staff)

external = staff.difference({"Kelly"})
print(external)

staff = staff.intersection({"Kelly", "Bob"})
print(staff)

staff = staff.symmetric_difference(directors)
print(staff)
#TASK5
vowels = {"a", "e", "i"}
vowels = vowels.union("o", "u")
#