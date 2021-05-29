import numpy as np 

def function(x):

	v4 = 0
	a2 = x
	x = 7
	paths = []
	try:
		if x <= 5:
			x = x-2
			x = 0+x
			a2 = 8+9
			paths.append(1)
		else:
			x = v4-x
			v4 = 9*v4
			paths.append(2)
		if v4 >= 0:
			x = 1+x
			a2 = a2*5
			paths.append(3)
		else:
			v4 = v4*5
			x = x+5
			x = 8/x
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