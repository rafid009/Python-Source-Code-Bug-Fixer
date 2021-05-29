import numpy as np 

def function(x):

	e4 = 4
	v7 = x
	paths = []
	try:
		if e4 <= 3:
			v7 = x+x
			v7 = 9/v7
			paths.append(1)
		else:
			v7 = v7+6
			e4 = 9*e4
			paths.append(2)
		if x >= 8:
			v7 = v7+2
			e4 = e4-1
			x = x+4
			paths.append(3)
		else:
			e4 = e4*8
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