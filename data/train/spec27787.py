import numpy as np 

def function(x):

	t0 = x
	a3 = x
	x = x
	paths = []
	try:
		if a3 > 9:
			a3 = a3+2
			paths.append(1)
		else:
			t0 = t0-6
			a3 = 2/t0
			paths.append(2)
		if a3 > 7:
			a3 = a3/4
			t0 = t0*9
			x = a3-a3
			paths.append(3)
		else:
			a3 = 7-a3
			x = 0+x
			a3 = x*6
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