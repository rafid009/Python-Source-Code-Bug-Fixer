import numpy as np 

def function(x):

	j0 = x
	g5 = 1
	paths = []
	try:
		if j0 < 8:
			x = 1*x
			g5 = g5-1
			paths.append(1)
		else:
			j0 = j0/j0
			g5 = g5-g5
			paths.append(2)
		if x < 6:
			g5 = 7*g5
			x = x*4
			paths.append(3)
		else:
			g5 = 2*1
			g5 = 9*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j0 = x**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))