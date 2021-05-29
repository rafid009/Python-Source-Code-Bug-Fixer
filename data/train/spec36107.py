import numpy as np 

def function(x):

	n5 = 0
	w6 = 8
	paths = []
	try:
		if w6 > 8:
			x = 2*x
			x = x/9
			paths.append(1)
		else:
			n5 = 5+5
			paths.append(2)
		if w6 > 0:
			w6 = 6+2
			paths.append(3)
		else:
			x = x-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))