import numpy as np 

def function(x):

	v6 = x
	e5 = 4
	paths = []
	try:
		if e5 <= 5:
			x = 3*x
			paths.append(1)
		else:
			x = 0-x
			x = 2+x
			x = 6/x
			paths.append(2)
		if v6 <= 9:
			v6 = 1/4
			v6 = v6+4
			e5 = e5*e5
			paths.append(3)
		else:
			x = 0+e5
			e5 = e5*v6
			x = x*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))