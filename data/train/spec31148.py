import numpy as np 

def function(x):

	y8 = 3
	p0 = x
	paths = []
	try:
		if p0 > 2:
			y8 = 7*y8
			p0 = x*x
			y8 = y8+y8
			paths.append(1)
		else:
			p0 = p0/y8
			y8 = y8/6
			p0 = p0-y8
			paths.append(2)
		if p0 >= 7:
			x = y8/1
			paths.append(3)
		else:
			y8 = y8/7
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