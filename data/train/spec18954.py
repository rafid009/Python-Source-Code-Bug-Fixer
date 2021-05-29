import numpy as np 

def function(x):

	y5 = x
	o0 = 6
	paths = []
	try:
		if y5 >= 9:
			y5 = o0-5
			y5 = y5+9
			paths.append(1)
		else:
			o0 = 4*5
			o0 = 8+o0
			paths.append(2)
		if x >= 2:
			x = 2-x
			o0 = 7+x
			paths.append(3)
		else:
			y5 = 3/2
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