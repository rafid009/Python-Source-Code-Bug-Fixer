import numpy as np 

def function(x):

	h1 = x
	p9 = x
	x = 1
	paths = []
	try:
		if h1 > 8:
			x = x+8
			h1 = 8+2
			paths.append(1)
		else:
			p9 = 0-p9
			x = x/x
			paths.append(2)
		if x > 4:
			h1 = h1+4
			paths.append(3)
		else:
			x = x*1
			p9 = 9+5
			x = 7-h1
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