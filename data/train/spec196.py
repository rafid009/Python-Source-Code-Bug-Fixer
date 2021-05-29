import numpy as np 

def function(x):

	v5 = x
	a9 = x
	paths = []
	try:
		if a9 <= 2:
			v5 = v5-x
			a9 = a9*2
			v5 = v5/3
			paths.append(1)
		else:
			v5 = 1+v5
			paths.append(2)
		if v5 <= 6:
			x = 4-a9
			paths.append(3)
		else:
			v5 = 4+a9
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