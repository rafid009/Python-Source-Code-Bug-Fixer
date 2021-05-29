import numpy as np 

def function(x):

	f6 = 4
	x5 = x
	x = 2
	paths = []
	try:
		if x < 9:
			f6 = f6*8
			x = x-f6
			paths.append(1)
		else:
			x5 = 3+x5
			x5 = x5-2
			paths.append(2)
		if x >= 4:
			f6 = 9+x
			x5 = f6+f6
			x = 7/3
			paths.append(3)
		else:
			f6 = x*x5
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