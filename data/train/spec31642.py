import numpy as np 

def function(x):

	v8 = x
	z4 = 5
	paths = []
	try:
		if z4 < 0:
			v8 = v8+z4
			paths.append(1)
		else:
			x = x/x
			v8 = v8+5
			paths.append(2)
		if z4 >= 6:
			x = 9*x
			paths.append(3)
		else:
			x = 3*8
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		z4 = v8**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))