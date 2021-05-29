import numpy as np 

def function(x):

	g2 = x
	h0 = 7
	paths = []
	try:
		if g2 >= 6:
			x = 1+x
			g2 = 8+8
			x = x*x
			paths.append(1)
		else:
			x = x-8
			paths.append(2)
		if h0 > 3:
			h0 = h0-x
			x = x+4
			x = x+7
			paths.append(3)
		else:
			g2 = x/g2
			x = x*5
			g2 = 3/g2
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		h0 = h0**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))