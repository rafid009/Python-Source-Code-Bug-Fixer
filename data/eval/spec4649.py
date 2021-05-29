import numpy as np 

def function(x):

	e8 = x
	v4 = 0
	paths = []
	try:
		if x > 2:
			x = 0-x
			e8 = 1-0
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if v4 < 4:
			x = v4-x
			paths.append(3)
		else:
			e8 = e8+e8
			v4 = 9*v4
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		v4 = e8**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))