import numpy as np 

def function(x):

	y3 = x
	paths = []
	try:
		if y3 >= 1:
			y3 = y3-3
			y3 = 6+y3
			y3 = y3*7
			paths.append(1)
		else:
			y3 = y3*x
			y3 = y3+8
			paths.append(2)
		if x > 2:
			y3 = y3+0
			y3 = y3-7
			y3 = 5*y3
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))