import numpy as np 

def function(x):

	h3 = x
	p2 = x
	paths = []
	try:
		if h3 <= 2:
			h3 = h3+6
			x = 4*x
			paths.append(1)
		else:
			p2 = 2+p2
			p2 = p2+5
			paths.append(2)
		if x >= 3:
			x = 1+x
			x = x/h3
			paths.append(3)
		else:
			p2 = 7*p2
			p2 = x+p2
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		h3 = p2**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))