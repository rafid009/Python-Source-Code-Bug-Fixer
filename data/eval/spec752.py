import numpy as np 

def function(x):

	e2 = 9
	k0 = 4
	paths = []
	try:
		if k0 <= 0:
			x = x-x
			x = x-x
			paths.append(1)
		else:
			x = x-9
			e2 = 8+e2
			paths.append(2)
		if x <= 6:
			e2 = x*9
			e2 = 6*8
			e2 = e2*x
			paths.append(3)
		else:
			x = x-x
			k0 = 3*x
			x = x+3
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		e2 = e2**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))