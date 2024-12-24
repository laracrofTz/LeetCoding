foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
ratings = [9, 9, 8, 15, 14, 7]

foodDict = {}
for i in range(len(foods)):
    foodDict[foods[i]] = (ratings[i], cuisines[i])

print(foodDict)
sortedFoodList = sorted(foodDict.items(), key=lambda r: r[1], reverse=True) # sort dictionary according to ratings
sortedFoodDict = dict(sortedFoodList)
print(sortedFoodDict)