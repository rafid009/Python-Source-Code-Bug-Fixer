import numpy as np 

def function(x):

	y5 = x
	o3 = 8
	paths = []
	try:
		if o3 >= 1:
			y5 = 0*8
			paths.append(1)
		else:
			x = x*y5
			paths.append(2)
		if y5 < 4:
			x = x*2
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y5 = x**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))