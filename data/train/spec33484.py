import numpy as np 

def function(x):

	v2 = x
	a8 = 1
	paths = []
	try:
		if v2 < 6:
			v2 = a8+v2
			x = x+9
			a8 = 6/x
			paths.append(1)
		else:
			v2 = x/5
			paths.append(2)
		if v2 >= 0:
			v2 = v2-2
			x = x-4
			paths.append(3)
		else:
			v2 = 2-v2
			x = x/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))