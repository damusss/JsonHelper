from json_helper import *
from random import choice, randint

def GetKey():
    s = ""
    s+= choice(list(letters))
    return s

json = Json.Root()

letters = "abcdefghijklmnopqrstuvwxyz"

pair = JsonPair("first",JsonValue(JsonType.Number,randint(0,15765)))

for i in range(3000):
    newP = pair.Copy()
    newP.SetKey(GetKey())
    newP.value.Set(randint(0,15765))
    json.Add(newP)

print(json.ContainsDuplicate("a"))
json.RemoveDuplicates()
print(json.ContainsDuplicate("a"))
Json.SaveObject(json,"test.json")