import numpy as np 

def function(x):

	a0 = 7
	w9 = x
	x = 1
	paths = []
	try:
		if a0 < 4:
			x = 5-9
			x = x/6
			paths.append(1)
		else:
			a0 = 9*a0
			a0 = 0/a0
			a0 = a0*w9
			paths.append(2)
		if x <= 7:
			x = w9/8
			a0 = 4/8
			w9 = x/w9
			paths.append(3)
		else:
			w9 = w9*a0
			a0 = a0*6
			a0 = w9-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))