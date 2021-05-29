import numpy as np 

def function(x):

	h9 = x
	p0 = 3
	paths = []
	try:
		if p0 > 7:
			p0 = 5-p0
			x = x*x
			x = 5*1
			paths.append(1)
		else:
			h9 = 4+h9
			p0 = 1-p0
			paths.append(2)
		if x > 0:
			h9 = h9*0
			paths.append(3)
		else:
			h9 = h9-p0
			p0 = h9+4
			p0 = 5/6
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		h9 = p0**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))