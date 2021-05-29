import numpy as np 

def function(x):

	h6 = x
	p7 = x
	paths = []
	try:
		if x <= 1:
			h6 = h6*p7
			paths.append(1)
		else:
			h6 = x-p7
			paths.append(2)
		if p7 > 3:
			p7 = p7/8
			h6 = h6-8
			h6 = 0*x
			paths.append(3)
		else:
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		x = p7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))