import numpy as np 

def function(x):

	f9 = 2
	y3 = 5
	paths = []
	try:
		if y3 <= 7:
			y3 = 6*y3
			f9 = f9/5
			y3 = y3*x
			paths.append(1)
		else:
			x = x/y3
			y3 = y3*x
			paths.append(2)
		if f9 < 9:
			f9 = y3+2
			paths.append(3)
		else:
			x = 5-8
			f9 = f9-9
			x = 9-x
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