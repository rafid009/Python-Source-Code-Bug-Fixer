import numpy as np 

def function(x):

	a8 = 4
	v7 = x
	paths = []
	try:
		if v7 > 3:
			x = x/3
			paths.append(1)
		else:
			v7 = v7+5
			paths.append(2)
		if x <= 5:
			a8 = a8-5
			a8 = a8+8
			paths.append(3)
		else:
			v7 = 3+v7
			x = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))