import numpy as np 

def function(x):

	v7 = 6
	a2 = 8
	paths = []
	try:
		if v7 > 6:
			v7 = v7-1
			paths.append(1)
		else:
			a2 = a2+v7
			paths.append(2)
		if v7 <= 5:
			v7 = v7*5
			paths.append(3)
		else:
			a2 = a2/3
			a2 = x-4
			a2 = a2+v7
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