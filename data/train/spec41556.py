import numpy as np 

def function(x):

	g4 = x
	j8 = 5
	paths = []
	try:
		if x <= 8:
			j8 = 9/j8
			x = x/x
			x = x/5
			paths.append(1)
		else:
			g4 = g4*1
			j8 = 0-6
			paths.append(2)
		if j8 <= 2:
			j8 = j8*j8
			x = 8-x
			j8 = j8-8
			paths.append(3)
		else:
			x = g4-j8
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