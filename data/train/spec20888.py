import numpy as np 

def function(x):

	w7 = x
	a0 = x
	paths = []
	try:
		if w7 > 9:
			a0 = 8-a0
			x = x-x
			w7 = x/a0
			paths.append(1)
		else:
			a0 = x/a0
			a0 = a0*3
			paths.append(2)
		if x > 7:
			x = x+3
			paths.append(3)
		else:
			a0 = a0*8
			a0 = 1-w7
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w7 = x**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))