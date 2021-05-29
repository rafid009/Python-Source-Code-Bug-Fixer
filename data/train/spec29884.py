import numpy as np 

def function(x):

	p4 = 9
	h3 = 9
	paths = []
	try:
		if p4 <= 7:
			p4 = p4-p4
			h3 = 7+p4
			h3 = p4+h3
			paths.append(1)
		else:
			p4 = x*p4
			paths.append(2)
		if h3 <= 4:
			x = x*h3
			x = x/7
			paths.append(3)
		else:
			x = x*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))