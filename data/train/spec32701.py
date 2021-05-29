import numpy as np 

def function(x):

	p4 = 2
	h6 = 4
	paths = []
	try:
		if x > 2:
			x = x+2
			h6 = 0+0
			x = h6-x
			paths.append(1)
		else:
			x = x*h6
			paths.append(2)
		if x <= 1:
			h6 = h6*2
			p4 = x+h6
			paths.append(3)
		else:
			p4 = p4*5
			h6 = h6-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p4 = x**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))