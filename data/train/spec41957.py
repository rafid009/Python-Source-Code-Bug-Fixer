import numpy as np 

def function(x):

	w5 = 5
	x4 = x
	paths = []
	try:
		if x4 > 8:
			x = x/2
			x = x-w5
			paths.append(1)
		else:
			x = x-6
			x = x+x
			paths.append(2)
		if x <= 1:
			w5 = x*9
			x4 = 4*x4
			paths.append(3)
		else:
			w5 = w5+w5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x4 = x**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))