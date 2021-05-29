import numpy as np 

def function(x):

	n2 = 5
	w9 = 7
	paths = []
	try:
		if n2 <= 7:
			x = x-w9
			paths.append(1)
		else:
			n2 = 4*n2
			w9 = x/x
			x = x-3
			paths.append(2)
		if x >= 4:
			w9 = w9-6
			x = 4*9
			x = x+w9
			paths.append(3)
		else:
			w9 = 6/1
			w9 = x*n2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n2 = x**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))