import numpy as np 

def function(x):

	g4 = 7
	h2 = 1
	paths = []
	try:
		if g4 > 1:
			h2 = x+h2
			h2 = 2/3
			paths.append(1)
		else:
			h2 = 3*h2
			g4 = g4*h2
			paths.append(2)
		if x <= 7:
			g4 = g4*2
			paths.append(3)
		else:
			x = x/1
			g4 = 1+x
			h2 = h2+1
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