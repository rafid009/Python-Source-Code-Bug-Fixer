import numpy as np 

def function(x):

	g3 = 1
	h1 = 5
	paths = []
	try:
		if g3 > 9:
			g3 = g3-h1
			paths.append(1)
		else:
			g3 = g3*2
			g3 = g3+g3
			paths.append(2)
		if h1 >= 5:
			h1 = h1-9
			g3 = g3+g3
			x = x+9
			paths.append(3)
		else:
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		h1 = h1**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))