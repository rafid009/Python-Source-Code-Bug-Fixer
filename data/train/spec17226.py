import numpy as np 

def function(x):

	g3 = 2
	j2 = x
	paths = []
	try:
		if x < 6:
			g3 = 3+1
			paths.append(1)
		else:
			g3 = 2/9
			x = x+g3
			g3 = g3-2
			paths.append(2)
		if g3 <= 0:
			g3 = g3+2
			g3 = g3+g3
			j2 = 8+j2
			paths.append(3)
		else:
			j2 = 3/8
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))