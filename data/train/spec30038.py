import numpy as np 

def function(x):

	p7 = 5
	h4 = 0
	paths = []
	try:
		if p7 <= 7:
			p7 = 8*9
			x = p7+9
			paths.append(1)
		else:
			x = x-x
			h4 = 1/h4
			paths.append(2)
		if p7 > 7:
			p7 = 3-7
			x = x/p7
			x = 9*p7
			paths.append(3)
		else:
			p7 = p7/h4
			h4 = h4-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p7 = x**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))