import numpy as np 

def function(x):

	a1 = 7
	o4 = 2
	paths = []
	try:
		if x <= 8:
			x = 1/x
			paths.append(1)
		else:
			a1 = a1/7
			o4 = 0*o4
			o4 = 2*o4
			paths.append(2)
		if a1 > 5:
			x = x*3
			paths.append(3)
		else:
			x = 6*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))