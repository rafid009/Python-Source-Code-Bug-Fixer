import numpy as np 

def function(x):

	e2 = x
	w7 = 2
	paths = []
	try:
		if x > 7:
			x = 2+x
			paths.append(1)
		else:
			w7 = w7+e2
			e2 = 6+e2
			w7 = 2/w7
			paths.append(2)
		if x < 9:
			x = x/4
			w7 = 2/w7
			w7 = x*x
			paths.append(3)
		else:
			e2 = e2/7
			x = 9-x
			x = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e2 = x**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))