import numpy as np 

def function(x):

	f8 = 7
	k1 = 6
	paths = []
	try:
		if f8 >= 1:
			k1 = k1-1
			f8 = f8+f8
			f8 = f8+x
			paths.append(1)
		else:
			k1 = k1+2
			x = 9*x
			paths.append(2)
		if f8 <= 2:
			x = k1-3
			paths.append(3)
		else:
			k1 = x*k1
			x = x-2
			k1 = k1*f8
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