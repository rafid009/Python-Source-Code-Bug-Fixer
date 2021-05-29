import numpy as np 

def function(x):

	c6 = 5
	t6 = x
	paths = []
	try:
		if c6 <= 4:
			x = c6+7
			x = 6/x
			paths.append(1)
		else:
			x = 3-x
			paths.append(2)
		if c6 >= 8:
			c6 = c6-x
			x = t6-t6
			paths.append(3)
		else:
			x = 4+2
			c6 = c6*x
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		t6 = t6**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))