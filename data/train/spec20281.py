import numpy as np 

def function(x):

	v6 = x
	y6 = x
	paths = []
	try:
		if y6 > 6:
			v6 = x-v6
			x = y6-6
			x = x+x
			paths.append(1)
		else:
			y6 = y6/y6
			x = x+6
			paths.append(2)
		if y6 >= 5:
			v6 = x+y6
			v6 = 6/2
			x = x*y6
			paths.append(3)
		else:
			x = v6+x
			y6 = 4+3
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