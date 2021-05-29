import numpy as np 

def function(x):

	v4 = 5
	x2 = 6
	paths = []
	try:
		if x2 < 4:
			x = 2+9
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if x < 8:
			x2 = 2-x
			x2 = x2-3
			x = x+7
			paths.append(3)
		else:
			x2 = x2*3
			x2 = 3-x2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v4 = x**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))