import numpy as np 

def function(x):

	g8 = 7
	e0 = x
	paths = []
	try:
		if g8 > 5:
			e0 = e0-7
			x = 8/x
			paths.append(1)
		else:
			g8 = 6*g8
			e0 = 2+5
			paths.append(2)
		if e0 > 3:
			g8 = 4*g8
			e0 = e0*2
			e0 = 7*e0
			paths.append(3)
		else:
			e0 = 8+e0
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		e0 = e0**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))