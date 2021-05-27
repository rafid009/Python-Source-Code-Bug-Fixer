import numpy as np 

def function(x):

	h4 = 7
	p6 = 8
	paths = []
	try:
		if p6 < 6:
			p6 = p6*0
			p6 = 3-p6
			h4 = 8*h4
			paths.append(1)
		else:
			p6 = x/9
			h4 = 0+h4
			paths.append(2)
		if h4 < 2:
			h4 = 3-h4
			h4 = 3-h4
			paths.append(3)
		else:
			h4 = h4+p6
			h4 = h4/5
			p6 = 6*p6
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