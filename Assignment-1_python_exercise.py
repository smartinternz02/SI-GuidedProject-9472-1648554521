#!/usr/bin/env python
# coding: utf-8

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[1]:


a=4
b=7
print(a^b)


# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

# In[3]:


a="HI there Sam"
print(a.split())


# In[4]:


b="Hi there dad"
print(b.split())


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[6]:


planet="Earth"
diameter=12742
print(f"The diameter of{planet} is {diameter}kilometers.")


# In[7]:


print(f"The diameter of{planet} is {diameter}kilometers.")


# ** Given this nested list, use indexing to grab the word "hello" **

# In[ ]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[9]:


lst1 = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
lst1[3][1][2]


# ** Given this nest dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[15]:


d={'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[16]:



print(d['k1'][3]['tricky'][3]['target'][3])


# ** What is the main difference between a tuple and a list? **

# tuple is immutable where as list is mutable.

# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[18]:


a="user@domain.com"
l=a.split('@')
print(l[1])


# In[19]:


print(l[1])


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[24]:


a="dog is dangerous"
if 'dog'in a:
    print("True")


# In[ ]:





# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[37]:


str="dog is harmful and dog is helpful in some cases"
c=0
for a in str.lower().split():
    if a=="dog":
        c=c+1
print(c)


# In[ ]:





# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[31]:


def caught_speeding(speed, is_birthday):
    
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed
    
    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'


# In[34]:


caught_speeding(86,True)


# In[38]:


caught_speeding(70,True)


# # Great job!
