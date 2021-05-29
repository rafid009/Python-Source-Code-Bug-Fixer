import numpy as np 

def function(x):

	p0 = x
	h6 = 7
	paths = []
	try:
		if x > 7:
			p0 = 1+x
			paths.append(1)
		else:
			x = x/8
			p0 = p0-5
			paths.append(2)
		if p0 > 3:
			h6 = 2/h6
			paths.append(3)
		else:
			p0 = 8/p0
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		x = p0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))