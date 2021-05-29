import numpy as np 

def function(x):

	z2 = 3
	e8 = 4
	x = 1
	paths = []
	try:
		if e8 > 0:
			e8 = z2+z2
			x = 4/9
			e8 = e8-e8
			paths.append(1)
		else:
			x = x/8
			e8 = 5/e8
			paths.append(2)
		if x >= 0:
			x = x/4
			x = x-3
			paths.append(3)
		else:
			x = 4*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z2 = x**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))