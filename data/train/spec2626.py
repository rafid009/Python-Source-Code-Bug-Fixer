import numpy as np 

def function(x):

	g3 = 6
	h7 = x
	paths = []
	try:
		if x < 5:
			h7 = 0/h7
			h7 = 3+h7
			paths.append(1)
		else:
			x = h7*3
			h7 = x+9
			paths.append(2)
		if g3 > 4:
			x = x-2
			paths.append(3)
		else:
			x = 7+3
			g3 = h7*2
			g3 = g3/6
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