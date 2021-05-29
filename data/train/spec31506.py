import numpy as np 

def function(x):

	v6 = x
	c8 = x
	paths = []
	try:
		if v6 < 4:
			c8 = 5+x
			paths.append(1)
		else:
			x = 8*x
			v6 = v6-6
			x = 7-4
			paths.append(2)
		if c8 >= 2:
			v6 = 6*v6
			c8 = c8/c8
			paths.append(3)
		else:
			v6 = 6*x
			v6 = v6-8
			v6 = 8-v6
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))