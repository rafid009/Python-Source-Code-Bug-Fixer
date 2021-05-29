import numpy as np 

def function(x):

	w3 = x
	a2 = 4
	paths = []
	try:
		if a2 > 7:
			x = a2/x
			paths.append(1)
		else:
			w3 = 7-w3
			a2 = w3-7
			paths.append(2)
		if x <= 2:
			x = 3/8
			paths.append(3)
		else:
			w3 = a2*6
			x = 9*x
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))