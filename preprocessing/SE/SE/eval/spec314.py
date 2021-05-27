import numpy as np 

def function(x):

	w7 = x
	e6 = x
	paths = []
	try:
		if e6 < 3:
			w7 = 9+6
			paths.append(1)
		else:
			e6 = e6+2
			paths.append(2)
		if w7 >= 9:
			w7 = w7*6
			x = x/w7
			x = x+x
			paths.append(3)
		else:
			x = x*x
			e6 = 7-e6
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