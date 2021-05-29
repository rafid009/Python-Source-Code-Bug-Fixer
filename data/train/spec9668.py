import numpy as np 

def function(x):

	v5 = 5
	c4 = 9
	paths = []
	try:
		if v5 < 7:
			v5 = v5/9
			paths.append(1)
		else:
			x = x*x
			c4 = c4*v5
			paths.append(2)
		if v5 <= 7:
			v5 = 8+v5
			paths.append(3)
		else:
			x = c4*2
			c4 = v5*2
			c4 = c4/v5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))