import numpy as np 

def function(x):

	c7 = x
	a9 = 7
	paths = []
	try:
		if a9 <= 9:
			a9 = c7-a9
			paths.append(1)
		else:
			a9 = 4/a9
			x = x+7
			c7 = c7-c7
			paths.append(2)
		if a9 > 3:
			x = 7*x
			paths.append(3)
		else:
			x = x+0
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		a9 = c7**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))