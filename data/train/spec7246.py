import numpy as np 

def function(x):

	c5 = x
	v9 = x
	paths = []
	try:
		if c5 > 7:
			c5 = c5-2
			c5 = c5/6
			x = 3*x
			paths.append(1)
		else:
			v9 = v9*6
			x = x+v9
			x = 6-x
			paths.append(2)
		if c5 < 8:
			v9 = 6*v9
			paths.append(3)
		else:
			c5 = c5+c5
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		v9 = v9**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))