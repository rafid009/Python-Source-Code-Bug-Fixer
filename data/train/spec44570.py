import numpy as np 

def function(x):

	w9 = x
	e4 = 3
	paths = []
	try:
		if e4 > 1:
			w9 = w9*8
			paths.append(1)
		else:
			e4 = 7/3
			e4 = e4-8
			paths.append(2)
		if w9 >= 5:
			x = x*4
			w9 = w9*e4
			paths.append(3)
		else:
			x = x+4
			e4 = w9-e4
			e4 = 2+e4
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		e4 = w9**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))