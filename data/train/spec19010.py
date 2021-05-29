import numpy as np 

def function(x):

	p0 = x
	k2 = 1
	paths = []
	try:
		if x > 0:
			x = x/2
			k2 = k2*7
			x = x+1
			paths.append(1)
		else:
			k2 = k2/9
			p0 = p0*4
			paths.append(2)
		if p0 < 6:
			k2 = k2+p0
			p0 = 8+p0
			paths.append(3)
		else:
			k2 = k2-2
			x = x+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k2 = x**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))