import numpy as np 

def function(x):

	a8 = 3
	c2 = x
	paths = []
	try:
		if a8 >= 3:
			a8 = 6*a8
			a8 = 4*1
			paths.append(1)
		else:
			c2 = 1*c2
			x = x-x
			paths.append(2)
		if x <= 5:
			a8 = x/a8
			x = 2/9
			paths.append(3)
		else:
			x = 7-x
			x = x+x
			x = x/x
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))