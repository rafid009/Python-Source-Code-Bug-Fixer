import numpy as np 

def function(x):

	c1 = 3
	a9 = x
	paths = []
	try:
		if a9 >= 1:
			c1 = 8*c1
			paths.append(1)
		else:
			a9 = c1+a9
			paths.append(2)
		if a9 < 9:
			x = 1+2
			a9 = a9-1
			x = x+7
			paths.append(3)
		else:
			a9 = a9*4
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		a9 = a9**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))