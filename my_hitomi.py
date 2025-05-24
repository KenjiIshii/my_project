import requests
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
data = response.json()
print(data)

import matplotlib.pyplot as plt
X = [1,2,3,4,5]
Y = [2,4,6,8,10]

plt.plot(X,Y)
plt.title('Simple Line Graph')
plt.xlabel('X軸')
plt.ylabel('Y軸')
plt.grid(True)
plt.show()
 
# 棒グラフ
categories = ['A', 'B', 'C', 'D']
values = [10, 25, 15, 30]
 
plt.bar(categories, values)
plt.title('Bar Graph')
plt.show()
plt .savefig("graph.png")



for i in range(1, 101):
    if i % 3  == 0 and i % 5 == 0:
        print ("FizziBuzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print (i)
        
        
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(self . name + "がワン！と鳴いた")                  
pochi = Dog("ポチ")
pochi.bark()

