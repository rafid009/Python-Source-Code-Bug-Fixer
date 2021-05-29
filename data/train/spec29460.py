import numpy as np 

def function(x):

	h2 = 5
	p2 = x
	paths = []
	try:
		if x > 7:
			p2 = p2*3
			h2 = 0-h2
			h2 = h2+3
			paths.append(1)
		else:
			p2 = p2/3
			p2 = p2+8
			paths.append(2)
		if h2 >= 1:
			h2 = 5+p2
			h2 = 1/x
			paths.append(3)
		else:
			p2 = p2-7
			x = x*1
			h2 = h2/5
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		h2 = p2**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))