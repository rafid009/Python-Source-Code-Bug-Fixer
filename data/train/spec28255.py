import numpy as np 

def function(x):

	a6 = x
	g4 = 5
	paths = []
	try:
		if a6 < 6:
			x = 0-x
			a6 = a6+4
			a6 = 5/9
			paths.append(1)
		else:
			g4 = x*0
			a6 = 1+a6
			paths.append(2)
		if x >= 8:
			a6 = 3*a6
			x = x-x
			a6 = 4-a6
			paths.append(3)
		else:
			g4 = g4-1
			a6 = x-a6
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x = a6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))