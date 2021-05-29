import numpy as np 

def function(x):

	a4 = 7
	v6 = 3
	paths = []
	try:
		if a4 > 1:
			a4 = a4-3
			paths.append(1)
		else:
			v6 = v6+v6
			v6 = v6*v6
			paths.append(2)
		if x <= 6:
			x = x/9
			paths.append(3)
		else:
			v6 = v6*x
			v6 = 0+v6
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