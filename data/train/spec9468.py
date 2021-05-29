import numpy as np 

def function(x):

	p0 = 1
	x3 = 4
	paths = []
	try:
		if p0 >= 7:
			x = 7+x
			paths.append(1)
		else:
			p0 = 3*p0
			x = x*8
			p0 = x-0
			paths.append(2)
		if x < 0:
			x = x-3
			paths.append(3)
		else:
			x3 = 8/2
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