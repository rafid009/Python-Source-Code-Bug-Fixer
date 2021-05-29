import numpy as np 

def function(x):

	h8 = x
	p9 = 8
	paths = []
	try:
		if p9 > 2:
			x = 2/4
			paths.append(1)
		else:
			h8 = x+2
			paths.append(2)
		if p9 > 2:
			p9 = p9*x
			h8 = h8-x
			h8 = h8+0
			paths.append(3)
		else:
			h8 = h8*h8
			p9 = p9+6
			h8 = 7+0
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		x = h8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))