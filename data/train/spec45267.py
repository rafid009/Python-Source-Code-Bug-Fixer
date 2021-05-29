import numpy as np 

def function(x):

	c3 = x
	v2 = 1
	paths = []
	try:
		if c3 <= 8:
			v2 = v2*5
			v2 = 0/7
			v2 = v2-4
			paths.append(1)
		else:
			x = x*8
			c3 = 1-x
			x = 8+x
			paths.append(2)
		if x < 4:
			x = 4/x
			x = 6*c3
			paths.append(3)
		else:
			v2 = v2*5
			v2 = 5-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v2 = x**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))