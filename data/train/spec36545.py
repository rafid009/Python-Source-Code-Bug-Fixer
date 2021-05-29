import numpy as np 

def function(x):

	x9 = x
	p0 = x
	paths = []
	try:
		if p0 >= 8:
			p0 = 8*4
			x = x*4
			paths.append(1)
		else:
			x = x-5
			p0 = p0+x
			paths.append(2)
		if x > 6:
			x = 8/x
			x9 = 3/x9
			paths.append(3)
		else:
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))