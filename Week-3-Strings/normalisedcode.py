#This program is directly copied from the lab
#My own code wasn't getting the result so I wanted to see if it is correct

rawString=input("pleaseenterastring:")
normalisedString=rawString.strip().lower()

lenghtOfRawString=len(rawString)
lenghtOfNormalised=len(normalisedString)

print("ThatStringnormalisedis:{}".format(normalisedString))
print("wereducedtheinputstringfrom{}to{}characters".format(lenghtOfRawString,lenghtOfNormalised))

#It still didn't reduce down the number of characters
