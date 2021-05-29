import numpy as np 

def function(x):

	r4 = x
	f4 = 5
	paths = []
	try:
		if x < 8:
			f4 = 9-6
			paths.append(1)
		else:
			f4 = f4-7
			r4 = r4/r4
			paths.append(2)
		if f4 > 1:
			f4 = x+f4
			paths.append(3)
		else:
			x = x-x
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