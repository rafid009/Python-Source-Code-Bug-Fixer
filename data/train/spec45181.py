import numpy as np 

def function(x):

	w5 = x
	b9 = 4
	paths = []
	try:
		if x >= 9:
			x = 8*6
			paths.append(1)
		else:
			x = 7-b9
			paths.append(2)
		if x >= 9:
			w5 = 6+w5
			b9 = 1+9
			paths.append(3)
		else:
			w5 = w5*6
			b9 = 8*8
			x = x-8
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