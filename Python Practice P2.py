#!/usr/bin/env python
# coding: utf-8

# In[1]:


#booleans
True


# In[2]:


#Booleans
1 == 1


# In[3]:


#Booleans
1 == 2


# In[4]:


#Booleans
1 == 3


# In[5]:


#Booleans
2 == 2


# In[7]:


#Lists
my_list = [1,2,3,4]
print(my_list)


# In[8]:


#Sets
my_set = {1,2,3,4,5}
print(my_set)


# In[9]:


#Sets with len command
len(my_set)


# In[11]:


#Sets with len and print
my_set = {1,1,2,2}
len(my_set)
print(my_set)


# In[12]:


#Lists
[1,2] == [2,1]


# In[13]:


#Sets
{1,2,3} == {3,2,1,1,1}


# In[14]:


#Lists
[1,2] == [1,2]


# In[16]:


#Tuples
my_tuple = (1,2,3)

len(my_tuple)


# In[20]:


#Adding stuff to the list
da_list = ["a", "b", "c", "d"]
da_list.append("e")
print(da_list)


# In[33]:


#Dictionaries part 1
my_dictionary = {
    'a': 'apple',
    'b': 'brother'
    
}

my_dictionary['a']


# In[27]:


#Dictionaries part 2
ty_dictionary = {
    'apple': 'A red fruit', 
    'bear': 'A scary animal'
}

ty_dictionary['apple']


# In[35]:


20/6


# In[34]:


#Arithmetic Operators
20 % 6

#FAQ: Why is 20 % 6?  20/6 is 18 with a remainder of 2. This is used for mathematical operations.


# In[36]:


5 > 2


# In[37]:


5 < 2


# In[38]:


1 in [1,2,3,4,5]


# In[39]:


#IF/ELSE statements
a = True
if a:
    print('It is true!')
    print('Also print this')
else:
    print('It is false!')
print('Always print this')


# In[43]:


#IF/ELSE statements part 2
a = True
b = False
c = True
if a:
    print('It is true!')
    if b:
        print('Both are true')
        if c:
            print('All three are true')
else:
    print('It is false!')


# In[48]:


#Functions 
def multiplyByThree(val):
    return 3 * val

multiplyByThree(2)


# In[51]:


#Function part 2
def multiply(var1, var2):
    return var1 * var2


# In[52]:


multiply(2, 2)


# In[53]:


#Classes part 1a
class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4
    
    def speak(self):
        print(self.name + ' says: Bark!')


# In[55]:


#Classes part 1b
my_dog = Dog('Rover')
another_dog = Dog('Fluffy')

my_dog.speak()
another_dog.speak()


# In[57]:


#Classes part 2a
class Animal:
    
    alive = True
    def eat(self):
        print("Animal is eating.")
    def sleep(self):
        print("Animal is sleeping.")

class Rabbit(Animal):
    pass
class Fish(Animal):
    pass
class Hawk(Animal):
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()


# In[58]:


#Classes part 2b
rabbit.alive()


# In[61]:


# Challenge 2: Returns the value of the factorial of num if it is defined, otherwise, returns None
def factorial(num):
    if type(num) is not int:
        return None
    if num < 0:
        return None
    if num == 0:
        return 1
    
    i = 0
    f = 1
    while i < num:
        i = i + 1
        f = f * i
        
    return f

# Returns the value of the factorial of num if it is defined, otherwise, returns None
def factorial(num):
    if type(num) is not int:
        return None
    if num < 0:
        return None
    if num == 0:
        return 1
    
    return num * factorial(num - 1)


# In[64]:


# return 120
factorial(5)


# In[ ]:





# In[65]:


# return 720
factorial(6)


# In[ ]:


# return 1
factorial(0)


# In[ ]:


# return None
factorial('spam spam spam spam spam spam')


# In[66]:


#END OF PART 2 PRACTICE


# In[67]:


#Credit: 'Bro Code' https://www.youtube.com/watch?v=XKHEtdqhLK8&t=13888s&ab_channel=BroCode


# In[ ]:


#Credit: 'LinkedIn Learning Python Essentials training by Ryan Mitchell.'

