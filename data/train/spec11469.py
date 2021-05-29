import numpy as np 

def function(x):

	u1 = x
	w5 = 9
	paths = []
	try:
		if w5 > 4:
			w5 = 4*6
			w5 = w5/2
			w5 = 1/w5
			paths.append(1)
		else:
			w5 = 2/w5
			u1 = u1-9
			w5 = 6+5
			paths.append(2)
		if w5 > 4:
			w5 = 8/w5
			w5 = w5-1
			paths.append(3)
		else:
			u1 = x-u1
			u1 = w5+w5
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