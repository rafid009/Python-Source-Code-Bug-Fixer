import numpy as np 

def function(x):

	c3 = x
	v3 = x
	x = 3
	paths = []
	try:
		if c3 < 7:
			x = x/9
			paths.append(1)
		else:
			c3 = 7/7
			x = x*3
			paths.append(2)
		if c3 >= 3:
			x = 3*7
			c3 = 0+c3
			paths.append(3)
		else:
			x = x-v3
			c3 = c3+9
			x = 2-v3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		v3 = v3**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))