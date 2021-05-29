import numpy as np 

def function(x):

	e3 = 7
	a4 = 6
	paths = []
	try:
		if a4 > 9:
			a4 = 7/x
			paths.append(1)
		else:
			e3 = a4*8
			e3 = 6/x
			a4 = 6/a4
			paths.append(2)
		if a4 < 2:
			e3 = 8/e3
			x = x/a4
			a4 = 2+5
			paths.append(3)
		else:
			a4 = 1+x
			a4 = a4*x
			a4 = 1-e3
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))