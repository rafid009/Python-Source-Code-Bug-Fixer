import numpy as np 

def function(x):

	v1 = 0
	c7 = 5
	paths = []
	try:
		if c7 <= 0:
			v1 = v1+9
			c7 = c7-c7
			c7 = 7*x
			paths.append(1)
		else:
			x = 1-x
			paths.append(2)
		if v1 > 9:
			v1 = 2-0
			paths.append(3)
		else:
			v1 = v1-x
			c7 = x/5
			c7 = 3-c7
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		v1 = c7**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))