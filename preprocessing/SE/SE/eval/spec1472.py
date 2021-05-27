import numpy as np 

def function(x):

	y3 = x
	p0 = 9
	paths = []
	try:
		if x < 2:
			x = x*6
			paths.append(1)
		else:
			x = x*1
			x = 0+x
			y3 = y3/8
			paths.append(2)
		if x < 2:
			x = x-6
			y3 = 8/7
			paths.append(3)
		else:
			x = 8-7
			p0 = p0/2
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