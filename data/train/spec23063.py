import numpy as np 

def function(x):

	n6 = 6
	w5 = 6
	paths = []
	try:
		if n6 > 4:
			n6 = x-w5
			n6 = n6*5
			w5 = x-w5
			paths.append(1)
		else:
			w5 = w5*4
			paths.append(2)
		if n6 >= 3:
			w5 = 4+4
			x = x*3
			paths.append(3)
		else:
			x = x*3
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		n6 = n6**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))