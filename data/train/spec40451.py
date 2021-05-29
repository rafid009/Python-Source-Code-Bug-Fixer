import numpy as np 

def function(x):

	c7 = 6
	r7 = x
	paths = []
	try:
		if x <= 7:
			x = 9/4
			r7 = 6-1
			paths.append(1)
		else:
			c7 = c7-r7
			r7 = x/c7
			paths.append(2)
		if c7 >= 8:
			r7 = r7*3
			r7 = 0/r7
			r7 = 9-3
			paths.append(3)
		else:
			x = 6/2
			x = x-4
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		x = c7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))