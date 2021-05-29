import numpy as np 

def function(x):

	e5 = x
	w7 = 8
	x = 8
	paths = []
	try:
		if x > 8:
			w7 = w7-3
			w7 = 6-w7
			w7 = e5/w7
			paths.append(1)
		else:
			w7 = w7*w7
			x = 5/2
			e5 = 3*e5
			paths.append(2)
		if w7 >= 8:
			e5 = x*e5
			paths.append(3)
		else:
			e5 = 8/1
			x = 0-w7
			e5 = w7-1
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		w7 = e5**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))