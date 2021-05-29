import numpy as np 

def function(x):

	w0 = 5
	y3 = 9
	x = x
	paths = []
	try:
		if w0 >= 8:
			y3 = y3+y3
			paths.append(1)
		else:
			y3 = y3/y3
			paths.append(2)
		if w0 > 3:
			y3 = 1+x
			y3 = y3+8
			x = x-1
			paths.append(3)
		else:
			x = 5-x
			x = 8+5
			x = x/x
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