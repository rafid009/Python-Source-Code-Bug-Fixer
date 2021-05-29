import numpy as np 

def function(x):

	p0 = 1
	x2 = x
	x = x
	paths = []
	try:
		if x2 <= 4:
			p0 = 0+p0
			p0 = p0*9
			paths.append(1)
		else:
			p0 = 9*p0
			paths.append(2)
		if x2 <= 8:
			x = x*p0
			x2 = 9-2
			paths.append(3)
		else:
			x2 = x2-9
			x = x+8
			x = 9*7
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		p0 = x2**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))