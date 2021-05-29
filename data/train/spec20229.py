import numpy as np 

def function(x):

	i7 = x
	g5 = 8
	paths = []
	try:
		if x > 8:
			i7 = 8+x
			x = x+3
			i7 = 6+2
			paths.append(1)
		else:
			x = x+8
			paths.append(2)
		if g5 > 6:
			i7 = 5-9
			paths.append(3)
		else:
			g5 = 9*3
			x = 3*i7
			i7 = i7/i7
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