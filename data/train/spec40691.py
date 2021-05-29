import numpy as np 

def function(x):

	p3 = 4
	k0 = x
	paths = []
	try:
		if p3 <= 9:
			p3 = p3*6
			paths.append(1)
		else:
			x = k0-p3
			k0 = k0*4
			x = x-5
			paths.append(2)
		if x < 2:
			p3 = p3-k0
			p3 = 8+9
			k0 = p3/2
			paths.append(3)
		else:
			p3 = p3/k0
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))