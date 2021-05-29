import numpy as np 

def function(x):

	w9 = 1
	c7 = x
	paths = []
	try:
		if w9 >= 7:
			x = x*9
			x = w9+1
			c7 = c7+1
			paths.append(1)
		else:
			x = 3/9
			paths.append(2)
		if x < 3:
			c7 = c7+c7
			paths.append(3)
		else:
			c7 = c7*w9
			c7 = c7/w9
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		w9 = c7**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))