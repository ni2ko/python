print("#2-Boolean expressions")
check = []
print(check,'=',bool(check))
check = [0]
print(check,'=',bool(check))

print("#3-short circuit evaluation")
check = False
def func(item):
  print("In Function")
  return item
print("check = False, does not beyond and")
print(check and func(5))
print("func(5) > 3 is true, does not beyond or")
print((func(5) > 3) or func(0))

print("#4-numeric types")
whatType = eval(input('Enter a number: '))
if type(whatType) == int:
  print('{0} is int'.format(whatType))
if type(whatType) == float:
  print('{0} is float'.format(whatType))
if type(whatType) == complex:
  print('{0} is complex'.format(whatType))
print(type(123456789*123456789))

print('#5-strings')
string = "Example, Assignment"
print(string[1])
print(string[1:4])
print(string.split(","))

print("#6/7-arrays and lists")
array = [2,4,"yes", "no"]
array[0] = "not num"
array.append(34)
for x in array:
  print(x)

print("#8-tuples")
myTuple = (1,2,3,"End of Tuple")
myTuple += ("false add",)
for x in myTuple:
  print(x)

print("#9-slices")
example = "acbdefghijk"
print(example)
print(example[1:4])
print(example[-3:-1])

print("#10-index range checking")
newArray = [1,2,3,4,5,6]
index = 6
if -len(newArray) <= index < len(newArray):
  print(newArray[index])
index = 3
if -len(newArray) <= index < len(newArray):
  print(newArray[index])

print("#11-dictionaries")
dictionary = {
  "key1" : 1,
  "key2" : 2,
  "key3" : 3,
}
oxford = dictionary.copy()
oxford["next key"] = "new"
del oxford["key2"]
print(oxford)

print("#12-if statement")
if 2 > 2:
  print("2 > 4")
elif 2 < 2:
  print("2 < 2")
else:
  print("2 = 2")

print("#13/16/19-switch statement, indentationto denote code blocks, functions")
check = 1
def numInnumOut(number):
  switch = {
    1: "1-one",
    2: "2-two",
    3: "3-three",
  }
  return switch.get(number)
print(numInnumOut(3))

print("#14-for loop")
for x in range(10):
  print(x, "annoying orange")

print("#15-while loop")
num = 0
i = 0
while i < 10:
  num += i
  print(num)
  i += 1

print("#17/18/20-type binding and type checking and pass by reference vs. value")
a = 4
b = a
print("a = {0}".format(a))
print("b = {0}".format(b))
a = 3
print("a = {0}".format(a))
print("b = {0}".format(b))

