import numpy as np 

def function(x):

	b4 = x
	j1 = x
	paths = []
	try:
		if x < 1:
			j1 = j1+2
			j1 = 4+3
			b4 = 4+b4
			paths.append(1)
		else:
			x = 4*x
			j1 = j1+5
			paths.append(2)
		if b4 < 1:
			x = 8+b4
			paths.append(3)
		else:
			b4 = 9*5
			j1 = j1-x
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