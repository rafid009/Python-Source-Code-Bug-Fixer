import numpy as np 

def function(x):

	w5 = 1
	x4 = 9
	paths = []
	try:
		if x <= 4:
			x4 = 9+2
			w5 = x4/x
			paths.append(1)
		else:
			x = 4/2
			x4 = x4/x
			x4 = x4-1
			paths.append(2)
		if x4 > 2:
			x4 = x4/7
			w5 = w5-2
			w5 = x+1
			paths.append(3)
		else:
			x4 = 4-0
			x = w5+x4
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