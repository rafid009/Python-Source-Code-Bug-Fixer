import numpy as np 

def function(x):

	a7 = x
	w9 = x
	paths = []
	try:
		if x <= 8:
			x = x+8
			x = 3/x
			paths.append(1)
		else:
			a7 = a7/x
			x = a7*x
			a7 = a7-1
			paths.append(2)
		if w9 < 2:
			a7 = 1*a7
			paths.append(3)
		else:
			w9 = w9/5
			w9 = w9/3
			x = a7*7
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		a7 = a7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))