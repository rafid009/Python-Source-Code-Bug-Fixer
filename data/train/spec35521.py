import numpy as np 

def function(x):

	h3 = 2
	p0 = x
	paths = []
	try:
		if h3 < 2:
			h3 = h3*8
			p0 = 6+9
			h3 = 7/x
			paths.append(1)
		else:
			h3 = 9+x
			x = 0+h3
			p0 = p0-x
			paths.append(2)
		if p0 < 4:
			h3 = x/8
			paths.append(3)
		else:
			p0 = p0*p0
			h3 = 4-h3
			h3 = 8/x
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		p0 = h3**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))