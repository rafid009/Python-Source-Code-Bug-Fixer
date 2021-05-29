import numpy as np 

def function(x):

	w7 = 2
	l7 = 4
	paths = []
	try:
		if l7 <= 8:
			x = x-2
			w7 = w7*l7
			paths.append(1)
		else:
			w7 = w7/w7
			paths.append(2)
		if x > 0:
			w7 = w7+w7
			l7 = 6+l7
			w7 = 3*x
			paths.append(3)
		else:
			w7 = x-1
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