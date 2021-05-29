import numpy as np 

def function(x):

	h3 = 6
	p1 = 9
	paths = []
	try:
		if x < 6:
			p1 = p1+h3
			h3 = h3-1
			x = x/7
			paths.append(1)
		else:
			p1 = p1-3
			h3 = p1/h3
			p1 = x-p1
			paths.append(2)
		if h3 > 8:
			x = h3-5
			p1 = p1-8
			paths.append(3)
		else:
			h3 = h3-7
			p1 = h3/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p1 = x**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))