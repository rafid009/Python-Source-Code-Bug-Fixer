import numpy as np 

def function(x):

	o7 = 0
	a8 = 8
	paths = []
	try:
		if x > 8:
			x = 9/x
			paths.append(1)
		else:
			x = x*a8
			a8 = 2-a8
			paths.append(2)
		if x <= 0:
			o7 = a8+0
			paths.append(3)
		else:
			a8 = a8*1
			a8 = 4+a8
			a8 = a8-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))