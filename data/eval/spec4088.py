import numpy as np 

def function(x):

	a3 = 8
	o7 = 5
	paths = []
	try:
		if x < 2:
			x = a3/x
			paths.append(1)
		else:
			a3 = 3*x
			paths.append(2)
		if o7 <= 5:
			a3 = 5+0
			x = 6+x
			o7 = o7/6
			paths.append(3)
		else:
			o7 = o7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a3 = x**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))