import numpy as np 

def function(x):

	g4 = 6
	e8 = x
	x = x
	paths = []
	try:
		if e8 < 3:
			g4 = g4/g4
			paths.append(1)
		else:
			g4 = g4*9
			x = e8+x
			paths.append(2)
		if x <= 7:
			x = x-4
			e8 = e8*6
			x = x*e8
			paths.append(3)
		else:
			x = x+0
			g4 = g4/8
			e8 = g4+e8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e8 = x**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))