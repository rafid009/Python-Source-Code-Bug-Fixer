import numpy as np 

def function(x):

	g8 = 9
	j7 = 3
	paths = []
	try:
		if x < 4:
			x = x-9
			j7 = 8*j7
			paths.append(1)
		else:
			x = 4*x
			j7 = 8-j7
			paths.append(2)
		if j7 > 1:
			g8 = g8+x
			j7 = j7+9
			j7 = g8*9
			paths.append(3)
		else:
			g8 = x*g8
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