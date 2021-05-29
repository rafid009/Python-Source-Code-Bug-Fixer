import numpy as np 

def function(x):

	w3 = 4
	k4 = 8
	paths = []
	try:
		if x <= 4:
			k4 = 3/w3
			x = 9*x
			k4 = k4+2
			paths.append(1)
		else:
			x = 1+x
			k4 = 7/k4
			k4 = w3*w3
			paths.append(2)
		if k4 >= 4:
			w3 = x*x
			k4 = k4/3
			paths.append(3)
		else:
			k4 = k4-w3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))