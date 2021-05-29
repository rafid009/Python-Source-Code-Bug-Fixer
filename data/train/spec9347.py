import numpy as np 

def function(x):

	i0 = x
	y6 = x
	paths = []
	try:
		if y6 >= 6:
			i0 = i0+i0
			paths.append(1)
		else:
			x = i0+1
			y6 = 5+y6
			y6 = 2*y6
			paths.append(2)
		if y6 > 4:
			y6 = y6+6
			paths.append(3)
		else:
			y6 = 8/9
			x = x+1
			y6 = y6+0
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