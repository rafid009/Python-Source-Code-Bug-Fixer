import numpy as np 

def function(x):

	f7 = 3
	y6 = 9
	paths = []
	try:
		if x < 2:
			f7 = 3/2
			y6 = y6*5
			paths.append(1)
		else:
			f7 = 2/f7
			y6 = x+y6
			x = 2/4
			paths.append(2)
		if f7 < 7:
			y6 = y6+4
			f7 = f7-5
			x = f7*x
			paths.append(3)
		else:
			x = 2*7
			y6 = x/f7
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