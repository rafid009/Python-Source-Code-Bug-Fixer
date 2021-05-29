import numpy as np 

def function(x):

	e2 = 4
	v6 = 8
	paths = []
	try:
		if v6 >= 6:
			e2 = v6*7
			x = x*5
			paths.append(1)
		else:
			e2 = x*3
			x = 7/v6
			v6 = 9/x
			paths.append(2)
		if v6 < 4:
			x = x*8
			v6 = 5*v6
			e2 = e2+2
			paths.append(3)
		else:
			v6 = 7-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))