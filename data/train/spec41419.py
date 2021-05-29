import numpy as np 

def function(x):

	c9 = 0
	v2 = x
	paths = []
	try:
		if c9 < 5:
			c9 = 7-4
			v2 = v2*5
			paths.append(1)
		else:
			v2 = v2+9
			paths.append(2)
		if x >= 5:
			c9 = 1*c9
			paths.append(3)
		else:
			v2 = v2-0
			x = 5-x
			c9 = c9/8
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		v2 = v2**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))