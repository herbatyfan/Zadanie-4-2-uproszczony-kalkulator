# zadanie 4.2
word = []
list1 = []
list2 = []
word = str(input())
for letter in word:
     list1.append(letter)
     list2.append(letter)
list2.reverse()
print(list1 == list2)
