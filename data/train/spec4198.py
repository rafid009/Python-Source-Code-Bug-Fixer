import numpy as np 

def function(x):

	x3 = x
	p0 = 8
	paths = []
	try:
		if p0 < 0:
			x = 7*x3
			x3 = x3*9
			paths.append(1)
		else:
			x3 = 0*x3
			x3 = 3+x3
			paths.append(2)
		if x <= 2:
			x3 = 0+x
			x = 8/x
			p0 = x-p0
			paths.append(3)
		else:
			x3 = x3-1
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		x = p0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))