import numpy as np 

def function(x):

	c6 = x
	a5 = 9
	paths = []
	try:
		if x < 5:
			x = x+c6
			paths.append(1)
		else:
			a5 = a5/3
			x = 0*7
			a5 = 3-2
			paths.append(2)
		if a5 >= 4:
			x = 9-2
			x = a5-8
			a5 = x+2
			paths.append(3)
		else:
			c6 = a5/8
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		a5 = c6**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))