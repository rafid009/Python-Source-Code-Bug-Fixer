import numpy as np 

def function(x):

	c7 = x
	r8 = x
	paths = []
	try:
		if c7 > 5:
			r8 = r8/2
			x = x+8
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if x <= 1:
			c7 = 8/c7
			paths.append(3)
		else:
			c7 = c7-x
			x = 7+4
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		r8 = c7**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))