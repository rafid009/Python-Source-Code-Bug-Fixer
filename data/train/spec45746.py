import numpy as np 

def function(x):

	p0 = x
	j5 = x
	paths = []
	try:
		if p0 > 6:
			x = j5*8
			j5 = 8/9
			paths.append(1)
		else:
			x = 6/p0
			p0 = p0-p0
			x = j5+0
			paths.append(2)
		if p0 > 9:
			p0 = x/p0
			x = x*4
			j5 = 2-j5
			paths.append(3)
		else:
			x = 9/x
			j5 = 0-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))