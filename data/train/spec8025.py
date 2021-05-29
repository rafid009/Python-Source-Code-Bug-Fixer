import numpy as np 

def function(x):

	p0 = x
	k5 = x
	paths = []
	try:
		if k5 < 5:
			p0 = k5/p0
			k5 = k5/4
			paths.append(1)
		else:
			p0 = x+p0
			p0 = k5*4
			x = 5-p0
			paths.append(2)
		if k5 <= 9:
			k5 = 7*3
			paths.append(3)
		else:
			k5 = k5-k5
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