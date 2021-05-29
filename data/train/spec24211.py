import numpy as np 

def function(x):

	a9 = x
	w3 = 4
	paths = []
	try:
		if a9 > 2:
			x = 1+a9
			x = 0-x
			paths.append(1)
		else:
			w3 = w3/w3
			w3 = x-6
			x = 0*7
			paths.append(2)
		if a9 < 6:
			w3 = 2*w3
			w3 = 1-x
			w3 = x-1
			paths.append(3)
		else:
			x = x*6
			x = x-5
			x = x-6
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		x = a9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))