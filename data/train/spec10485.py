import numpy as np 

def function(x):

	p0 = x
	h3 = x
	x = x
	paths = []
	try:
		if h3 >= 7:
			p0 = p0-9
			paths.append(1)
		else:
			x = 9-x
			p0 = p0*0
			paths.append(2)
		if p0 >= 5:
			p0 = 1*p0
			h3 = h3-6
			p0 = p0-1
			paths.append(3)
		else:
			p0 = 8-9
			x = 5*8
			h3 = h3*7
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		x = h3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))