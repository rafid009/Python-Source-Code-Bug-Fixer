import numpy as np 

def function(x):

	v4 = x
	y4 = 5
	x = x
	paths = []
	try:
		if v4 < 6:
			x = x-5
			x = 1-x
			paths.append(1)
		else:
			x = x-x
			x = v4*y4
			v4 = v4/8
			paths.append(2)
		if v4 < 4:
			v4 = v4/4
			paths.append(3)
		else:
			x = x+8
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		x = v4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))