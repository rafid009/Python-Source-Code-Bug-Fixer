import numpy as np 

def function(x):

	a6 = x
	g4 = 1
	x = 3
	paths = []
	try:
		if g4 > 4:
			g4 = a6*0
			x = 4+x
			x = x-2
			paths.append(1)
		else:
			g4 = g4+x
			paths.append(2)
		if x <= 6:
			x = 9*x
			a6 = a6-g4
			x = x*x
			paths.append(3)
		else:
			a6 = 2/5
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