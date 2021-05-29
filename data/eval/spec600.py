import numpy as np 

def function(x):

	w9 = 4
	n1 = 6
	x = x
	paths = []
	try:
		if n1 <= 1:
			x = x/8
			w9 = w9+3
			x = w9*0
			paths.append(1)
		else:
			w9 = w9*x
			x = x/4
			n1 = n1-1
			paths.append(2)
		if n1 >= 6:
			n1 = 9-7
			w9 = n1*8
			paths.append(3)
		else:
			n1 = 4-6
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))