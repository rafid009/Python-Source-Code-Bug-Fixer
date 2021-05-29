import numpy as np 

def function(x):

	n4 = x
	y6 = 4
	paths = []
	try:
		if n4 >= 7:
			y6 = x-6
			n4 = n4+y6
			paths.append(1)
		else:
			x = n4+x
			x = x*y6
			paths.append(2)
		if x <= 3:
			y6 = y6/1
			n4 = n4/1
			paths.append(3)
		else:
			n4 = n4-7
			y6 = 1-7
			n4 = n4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y6 = x**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))