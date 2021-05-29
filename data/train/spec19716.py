import numpy as np 

def function(x):

	x3 = 4
	v2 = x
	paths = []
	try:
		if x < 6:
			v2 = v2*8
			paths.append(1)
		else:
			x3 = x3-x
			paths.append(2)
		if v2 > 1:
			x = 9-x
			paths.append(3)
		else:
			x3 = x3-2
			v2 = 0+5
			x3 = x-5
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x3 = x3**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))