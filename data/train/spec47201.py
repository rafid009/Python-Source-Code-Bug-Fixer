import numpy as np 

def function(x):

	v9 = x
	c4 = 3
	x = x
	paths = []
	try:
		if v9 < 4:
			c4 = x*x
			c4 = 1+c4
			x = c4/x
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if v9 >= 3:
			v9 = 3+7
			paths.append(3)
		else:
			x = x*8
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		c4 = v9**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))