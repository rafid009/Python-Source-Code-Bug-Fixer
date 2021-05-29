import numpy as np 

def function(x):

	j9 = 8
	w0 = 7
	paths = []
	try:
		if x > 3:
			x = x+w0
			x = w0-4
			w0 = w0*5
			paths.append(1)
		else:
			j9 = 2-9
			x = x+x
			x = 0-j9
			paths.append(2)
		if j9 >= 8:
			w0 = 7+x
			x = x-6
			j9 = 9+w0
			paths.append(3)
		else:
			j9 = j9-2
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