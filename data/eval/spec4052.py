import numpy as np 

def function(x):

	f0 = x
	w3 = 8
	paths = []
	try:
		if w3 >= 5:
			f0 = x/f0
			paths.append(1)
		else:
			f0 = f0*4
			w3 = w3/1
			paths.append(2)
		if x >= 3:
			x = 6/x
			w3 = w3*f0
			w3 = 2*w3
			paths.append(3)
		else:
			x = x*7
			x = x/2
			w3 = 6+9
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