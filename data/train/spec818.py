import numpy as np 

def function(x):

	n3 = x
	w6 = x
	paths = []
	try:
		if x > 4:
			w6 = w6/4
			x = 9-n3
			x = x*n3
			paths.append(1)
		else:
			x = w6-8
			w6 = 5/1
			paths.append(2)
		if x >= 3:
			x = n3-9
			w6 = x-8
			paths.append(3)
		else:
			x = n3*x
			x = 9+4
			x = 4-x
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