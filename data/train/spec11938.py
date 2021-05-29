import numpy as np 

def function(x):

	g5 = 0
	v1 = 4
	paths = []
	try:
		if v1 >= 3:
			g5 = g5+8
			v1 = 5*v1
			paths.append(1)
		else:
			g5 = g5-3
			g5 = 5-g5
			x = x/x
			paths.append(2)
		if v1 <= 1:
			v1 = v1+3
			v1 = x/3
			paths.append(3)
		else:
			g5 = g5/g5
			v1 = 5*g5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v1 = x**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))