import numpy as np 

def function(x):

	v5 = x
	e9 = 3
	paths = []
	try:
		if v5 > 4:
			e9 = 6-1
			paths.append(1)
		else:
			v5 = 5*v5
			paths.append(2)
		if v5 <= 4:
			x = 6*x
			v5 = 4+v5
			x = x+4
			paths.append(3)
		else:
			e9 = 0+e9
			x = x+1
			e9 = 4*e9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))