import numpy as np 

def function(x):

	n9 = 6
	y6 = x
	paths = []
	try:
		if x > 6:
			y6 = y6+5
			paths.append(1)
		else:
			y6 = 4/y6
			n9 = 6/9
			paths.append(2)
		if n9 < 5:
			n9 = n9/2
			n9 = 5-0
			y6 = x/y6
			paths.append(3)
		else:
			n9 = 1-n9
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