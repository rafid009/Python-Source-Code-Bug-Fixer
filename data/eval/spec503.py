import numpy as np 

def function(x):

	y2 = 3
	v1 = 4
	paths = []
	try:
		if x <= 7:
			x = x/7
			x = x+y2
			paths.append(1)
		else:
			v1 = 2/1
			paths.append(2)
		if v1 > 5:
			x = x/y2
			paths.append(3)
		else:
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y2 = x**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))