import numpy as np 

def function(x):

	q3 = x
	g3 = 9
	paths = []
	try:
		if x > 8:
			x = x+x
			g3 = g3/6
			paths.append(1)
		else:
			g3 = 1+g3
			paths.append(2)
		if x > 7:
			g3 = g3-g3
			x = x+x
			paths.append(3)
		else:
			g3 = g3+q3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q3 = x**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))