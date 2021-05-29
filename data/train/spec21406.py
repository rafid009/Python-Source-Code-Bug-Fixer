import numpy as np 

def function(x):

	w0 = x
	a2 = x
	x = 8
	paths = []
	try:
		if a2 <= 0:
			a2 = 8-a2
			a2 = w0*a2
			paths.append(1)
		else:
			w0 = 0*7
			w0 = w0*x
			paths.append(2)
		if w0 <= 7:
			x = x/1
			x = w0+x
			a2 = a2*9
			paths.append(3)
		else:
			x = x+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))