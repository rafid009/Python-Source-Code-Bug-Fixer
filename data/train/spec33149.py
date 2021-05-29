import numpy as np 

def function(x):

	j2 = x
	g8 = x
	paths = []
	try:
		if j2 > 9:
			j2 = x+8
			x = 8*x
			g8 = 4+x
			paths.append(1)
		else:
			j2 = j2*5
			paths.append(2)
		if x < 5:
			j2 = x+x
			paths.append(3)
		else:
			g8 = g8+7
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