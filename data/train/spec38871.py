import numpy as np 

def function(x):

	x4 = 6
	p0 = x
	paths = []
	try:
		if p0 > 0:
			p0 = x4-3
			x = x-4
			paths.append(1)
		else:
			x = 4-x
			paths.append(2)
		if x <= 7:
			x4 = 5-9
			paths.append(3)
		else:
			p0 = p0+x4
			x = x*x4
			x4 = 2-x4
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x4 = x4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))