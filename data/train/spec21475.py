import numpy as np 

def function(x):

	a6 = x
	y3 = 5
	paths = []
	try:
		if a6 <= 8:
			y3 = x*y3
			a6 = 4-x
			paths.append(1)
		else:
			y3 = 9+y3
			a6 = 6-0
			paths.append(2)
		if x <= 2:
			x = 7*x
			a6 = 0*1
			paths.append(3)
		else:
			a6 = 4-a6
			y3 = y3/6
			x = x/5
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