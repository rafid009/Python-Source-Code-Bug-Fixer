import numpy as np 

def function(x):

	c2 = 3
	v1 = 7
	paths = []
	try:
		if c2 > 7:
			x = x/3
			paths.append(1)
		else:
			v1 = v1/v1
			c2 = x/1
			v1 = 9*c2
			paths.append(2)
		if v1 > 6:
			v1 = 4+1
			c2 = v1/4
			paths.append(3)
		else:
			x = x/6
			v1 = 9-6
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		v1 = c2**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))