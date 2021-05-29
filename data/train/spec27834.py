import numpy as np 

def function(x):

	p9 = x
	h3 = 9
	paths = []
	try:
		if p9 <= 5:
			h3 = h3*p9
			paths.append(1)
		else:
			p9 = p9/4
			paths.append(2)
		if h3 < 6:
			p9 = 8*3
			paths.append(3)
		else:
			p9 = 3-x
			x = 1*h3
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p9 = x**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))