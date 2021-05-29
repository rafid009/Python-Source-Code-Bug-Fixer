import numpy as np 

def function(x):

	g5 = x
	e6 = 9
	paths = []
	try:
		if e6 < 8:
			g5 = 7+g5
			x = 3*x
			g5 = g5+1
			paths.append(1)
		else:
			e6 = 3+e6
			e6 = e6/g5
			g5 = g5+g5
			paths.append(2)
		if x >= 1:
			e6 = e6/2
			g5 = 0-0
			g5 = 3*g5
			paths.append(3)
		else:
			g5 = g5-1
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		e6 = g5**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))