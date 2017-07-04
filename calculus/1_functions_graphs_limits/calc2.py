import numpy as np
import matplotlib.pyplot as plt
# Example 2, sketching a scatter plot
# The amount A (in millions of dollars) spent on snowmobiles in the US from 1990 to 1999 (how old is this book?)
t = [1990,1991,1992,1993,1994,1995,1996,1997,1998,1999]
A = [322,362,391,515,715,910,974,975,957,958]

# I did a scatter chart last time, let's see if I can figure out bar graphs
width = 0.35
plt.bar(t,A, width, color="blue")
plt.show()