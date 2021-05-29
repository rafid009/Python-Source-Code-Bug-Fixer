import numpy as np 

def function(x):

	b7 = 7
	a4 = x
	paths = []
	try:
		if x > 2:
			x = a4*x
			x = x/6
			a4 = a4-a4
			paths.append(1)
		else:
			x = 9/x
			paths.append(2)
		if x > 9:
			x = 9/x
			a4 = a4+4
			paths.append(3)
		else:
			a4 = a4+6
			x = 5/a4
			a4 = a4*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))