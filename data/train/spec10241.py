import numpy as np 

def function(x):

	j2 = x
	g9 = 6
	paths = []
	try:
		if x < 1:
			g9 = 2-2
			x = x-g9
			paths.append(1)
		else:
			g9 = g9*6
			paths.append(2)
		if x <= 3:
			x = 6*x
			j2 = j2-0
			x = x/2
			paths.append(3)
		else:
			j2 = j2*7
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		g9 = j2**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))