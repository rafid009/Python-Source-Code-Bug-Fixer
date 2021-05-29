import numpy as np 

def function(x):

	g3 = x
	h6 = x
	paths = []
	try:
		if h6 > 4:
			g3 = 3-g3
			g3 = 4+g3
			g3 = x*g3
			paths.append(1)
		else:
			x = x/9
			h6 = g3-5
			paths.append(2)
		if g3 > 0:
			g3 = g3/x
			paths.append(3)
		else:
			g3 = h6/g3
			x = x*0
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		g3 = g3**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))