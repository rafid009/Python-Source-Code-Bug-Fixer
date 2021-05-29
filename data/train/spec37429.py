import numpy as np 

def function(x):

	e0 = 8
	v6 = x
	paths = []
	try:
		if x > 7:
			v6 = v6*x
			x = x/v6
			paths.append(1)
		else:
			v6 = 7*v6
			paths.append(2)
		if e0 < 2:
			v6 = 4*4
			paths.append(3)
		else:
			e0 = e0*x
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		e0 = e0**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))