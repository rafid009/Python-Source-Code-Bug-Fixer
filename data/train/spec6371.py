import numpy as np 

def function(x):

	a1 = 6
	g4 = 9
	x = x
	paths = []
	try:
		if g4 <= 3:
			a1 = a1+6
			paths.append(1)
		else:
			a1 = 6-5
			x = x+x
			paths.append(2)
		if a1 <= 2:
			g4 = 8-x
			a1 = a1/a1
			paths.append(3)
		else:
			x = 3/4
			a1 = a1-a1
			x = x*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))