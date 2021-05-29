import numpy as np 

def function(x):

	j8 = x
	g4 = 3
	paths = []
	try:
		if x < 7:
			j8 = 4*5
			j8 = 9/x
			paths.append(1)
		else:
			j8 = 7-3
			x = j8/9
			j8 = x/j8
			paths.append(2)
		if g4 <= 3:
			g4 = g4*x
			g4 = g4*9
			j8 = 9*g4
			paths.append(3)
		else:
			x = j8-0
			g4 = 9+g4
			j8 = j8+g4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j8 = x**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))