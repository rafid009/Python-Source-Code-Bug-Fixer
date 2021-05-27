import numpy as np 

def function(x):

	f6 = 8
	v3 = 3
	paths = []
	try:
		if x > 4:
			f6 = f6*8
			f6 = 7/7
			paths.append(1)
		else:
			f6 = 0+f6
			paths.append(2)
		if x <= 2:
			x = 3+x
			x = 9+x
			paths.append(3)
		else:
			f6 = 8/f6
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