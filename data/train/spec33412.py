import numpy as np 

def function(x):

	h6 = x
	p4 = 8
	paths = []
	try:
		if x <= 1:
			x = 2+2
			paths.append(1)
		else:
			p4 = p4*1
			x = 4-6
			x = x-6
			paths.append(2)
		if p4 > 5:
			p4 = 7+6
			x = 0-7
			paths.append(3)
		else:
			h6 = 7-h6
			h6 = 5+h6
			x = x+3
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