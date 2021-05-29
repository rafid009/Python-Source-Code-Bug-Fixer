import numpy as np 

def function(x):

	p0 = 0
	k2 = x
	x = 6
	paths = []
	try:
		if p0 > 3:
			k2 = 4/4
			p0 = 2*p0
			paths.append(1)
		else:
			p0 = k2-8
			x = 5-3
			paths.append(2)
		if x > 5:
			p0 = p0-x
			x = 8-x
			x = k2*x
			paths.append(3)
		else:
			p0 = p0*3
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		x = k2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))