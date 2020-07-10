# Simple dictionary(My First Python Program.)
d1={"alert":"the state of being watchful for possible danger.",
    "alone":"having no one else present.",
    "clown":"a comic entertainer",
    "emblem":"a heraldic device or symbolic object as a distinctive badge of a nation, organization, or family."}
print("Available words are - ",d1.keys(),"\nEnter the word: ")
a=input()
print(d1[a])
