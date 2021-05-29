import numpy as np 

def function(x):

	y6 = 5
	l3 = x
	paths = []
	try:
		if x >= 1:
			y6 = l3-9
			paths.append(1)
		else:
			y6 = l3-5
			paths.append(2)
		if x <= 8:
			x = x-9
			l3 = l3/x
			paths.append(3)
		else:
			l3 = 6/l3
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		y6 = l3**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))