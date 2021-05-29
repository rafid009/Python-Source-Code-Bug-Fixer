import numpy as np 

def function(x):

	e7 = 2
	g4 = 7
	paths = []
	try:
		if e7 <= 9:
			x = x/1
			g4 = 9*1
			paths.append(1)
		else:
			e7 = 5-e7
			x = x*x
			e7 = e7*0
			paths.append(2)
		if e7 > 8:
			x = g4-7
			paths.append(3)
		else:
			g4 = g4*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g4 = x**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))