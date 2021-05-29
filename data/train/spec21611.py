import numpy as np 

def function(x):

	h4 = x
	p7 = 8
	paths = []
	try:
		if x >= 8:
			x = x/5
			paths.append(1)
		else:
			p7 = p7+5
			x = 8*h4
			paths.append(2)
		if x <= 1:
			h4 = h4/9
			paths.append(3)
		else:
			p7 = 6*1
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