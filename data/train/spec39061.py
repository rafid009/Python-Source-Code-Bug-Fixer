import numpy as np 

def function(x):

	y5 = x
	q3 = 5
	paths = []
	try:
		if x >= 3:
			y5 = y5+0
			paths.append(1)
		else:
			q3 = 0+4
			paths.append(2)
		if y5 > 3:
			x = 7-7
			q3 = q3*2
			y5 = 4+y5
			paths.append(3)
		else:
			q3 = 0-q3
			q3 = 0*7
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