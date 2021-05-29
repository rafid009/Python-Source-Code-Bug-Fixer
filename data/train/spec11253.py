import numpy as np 

def function(x):

	e4 = 0
	g3 = x
	paths = []
	try:
		if x > 4:
			e4 = e4-g3
			paths.append(1)
		else:
			x = x+6
			x = x+x
			e4 = e4-e4
			paths.append(2)
		if x < 5:
			g3 = g3*x
			e4 = e4*5
			paths.append(3)
		else:
			x = g3/8
			g3 = e4+x
			g3 = g3+5
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		e4 = g3**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))