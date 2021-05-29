import numpy as np 

def function(x):

	e9 = 1
	w9 = x
	paths = []
	try:
		if x < 2:
			e9 = e9*9
			x = 4-5
			paths.append(1)
		else:
			e9 = e9/e9
			w9 = w9*5
			x = 8-x
			paths.append(2)
		if w9 < 6:
			e9 = 7-w9
			e9 = e9*8
			paths.append(3)
		else:
			x = e9/e9
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		e9 = w9**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))