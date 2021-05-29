import numpy as np 

def function(x):

	p0 = x
	k3 = 7
	paths = []
	try:
		if k3 < 8:
			p0 = 2*6
			paths.append(1)
		else:
			x = x-p0
			paths.append(2)
		if x < 7:
			k3 = 8*k3
			paths.append(3)
		else:
			k3 = 5*k3
			x = x*p0
			k3 = 0+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p0 = x**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))