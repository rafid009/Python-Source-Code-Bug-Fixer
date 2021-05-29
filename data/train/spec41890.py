import numpy as np 

def function(x):

	o6 = 5
	a0 = x
	paths = []
	try:
		if o6 < 8:
			x = 7/x
			a0 = 9/a0
			a0 = a0+2
			paths.append(1)
		else:
			x = x/5
			x = x-x
			paths.append(2)
		if a0 <= 1:
			x = x-1
			paths.append(3)
		else:
			a0 = o6+a0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))