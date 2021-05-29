import numpy as np 

def function(x):

	p2 = 2
	h2 = x
	paths = []
	try:
		if x > 8:
			x = h2+x
			p2 = p2/6
			p2 = 6*3
			paths.append(1)
		else:
			h2 = p2/h2
			x = x+2
			paths.append(2)
		if x <= 9:
			p2 = 3*p2
			h2 = 2/p2
			h2 = h2/5
			paths.append(3)
		else:
			p2 = p2+6
			h2 = 2-p2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h2 = x**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))