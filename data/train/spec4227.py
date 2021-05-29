import numpy as np 

def function(x):

	j7 = 5
	c7 = x
	paths = []
	try:
		if c7 > 0:
			c7 = x*2
			paths.append(1)
		else:
			j7 = 5/j7
			j7 = j7/1
			paths.append(2)
		if j7 >= 7:
			x = 3*x
			x = j7/5
			paths.append(3)
		else:
			j7 = 1/c7
			j7 = j7/4
			c7 = c7+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j7 = x**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))