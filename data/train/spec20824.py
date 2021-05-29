import numpy as np 

def function(x):

	g3 = 0
	a2 = x
	paths = []
	try:
		if g3 >= 0:
			x = 2/x
			paths.append(1)
		else:
			g3 = g3*g3
			paths.append(2)
		if a2 >= 6:
			x = x*2
			a2 = 3-7
			paths.append(3)
		else:
			a2 = 8*a2
			a2 = 7*x
			g3 = x-g3
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x = a2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))