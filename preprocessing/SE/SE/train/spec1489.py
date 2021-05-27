import numpy as np 

def function(x):

	v5 = x
	c3 = x
	paths = []
	try:
		if c3 > 2:
			c3 = c3-0
			c3 = c3-4
			x = x*5
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if x <= 6:
			v5 = v5-x
			v5 = v5/7
			v5 = v5+8
			paths.append(3)
		else:
			c3 = c3-2
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		v5 = c3**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))