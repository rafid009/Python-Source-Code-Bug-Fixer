import numpy as np 

def function(x):

	k3 = 2
	p0 = 6
	paths = []
	try:
		if p0 < 9:
			p0 = 7/5
			paths.append(1)
		else:
			p0 = p0+x
			paths.append(2)
		if x >= 9:
			p0 = 8+7
			p0 = x*p0
			k3 = 4+2
			paths.append(3)
		else:
			k3 = k3*p0
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