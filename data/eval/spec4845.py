import numpy as np 

def function(x):

	w1 = 2
	c7 = x
	x = x
	paths = []
	try:
		if x < 9:
			x = 0*x
			x = 8+x
			paths.append(1)
		else:
			c7 = c7+5
			paths.append(2)
		if x >= 7:
			x = 7*x
			paths.append(3)
		else:
			c7 = c7-x
			x = w1-x
			x = 0*5
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		w1 = c7**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))