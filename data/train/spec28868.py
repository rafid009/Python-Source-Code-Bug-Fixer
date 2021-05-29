import numpy as np 

def function(x):

	e4 = x
	v3 = x
	paths = []
	try:
		if x < 0:
			e4 = e4+6
			e4 = x+e4
			paths.append(1)
		else:
			e4 = 9/e4
			v3 = 6/v3
			v3 = 7-v3
			paths.append(2)
		if v3 < 9:
			x = x-e4
			v3 = 0*v3
			paths.append(3)
		else:
			v3 = 3+e4
			x = 5-x
			x = x*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v3 = x**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))