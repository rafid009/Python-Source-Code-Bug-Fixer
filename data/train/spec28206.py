import numpy as np 

def function(x):

	h0 = x
	p8 = 4
	x = 6
	paths = []
	try:
		if h0 <= 2:
			p8 = p8/h0
			paths.append(1)
		else:
			h0 = 3-0
			paths.append(2)
		if p8 <= 8:
			x = 8/h0
			x = x+4
			p8 = 0/p8
			paths.append(3)
		else:
			h0 = p8*h0
			x = x-4
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		p8 = h0**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))