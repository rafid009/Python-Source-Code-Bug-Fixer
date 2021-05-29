import numpy as np 

def function(x):

	h6 = 6
	g9 = x
	paths = []
	try:
		if g9 > 7:
			g9 = g9*9
			x = 0+x
			paths.append(1)
		else:
			h6 = h6-9
			g9 = 4+0
			paths.append(2)
		if x < 4:
			g9 = 2-g9
			h6 = h6/2
			h6 = 9*h6
			paths.append(3)
		else:
			x = x*1
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		g9 = h6**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))