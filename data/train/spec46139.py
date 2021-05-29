import numpy as np 

def function(x):

	a9 = x
	v2 = 1
	paths = []
	try:
		if v2 > 0:
			a9 = v2/6
			v2 = v2/8
			paths.append(1)
		else:
			v2 = v2/7
			paths.append(2)
		if v2 > 6:
			v2 = v2/9
			v2 = 2+0
			a9 = a9*9
			paths.append(3)
		else:
			x = x-a9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))