import numpy as np 

def function(x):

	p0 = 3
	k3 = x
	paths = []
	try:
		if k3 < 1:
			k3 = 0+4
			paths.append(1)
		else:
			p0 = p0*3
			p0 = p0-5
			paths.append(2)
		if x >= 5:
			k3 = p0-1
			k3 = 3/k3
			x = x*4
			paths.append(3)
		else:
			p0 = 7/p0
			p0 = p0+x
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		p0 = p0**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))