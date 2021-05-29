import numpy as np 

def function(x):

	a5 = 6
	p0 = 0
	x = x
	paths = []
	try:
		if x >= 6:
			x = a5-x
			a5 = a5*a5
			p0 = p0-3
			paths.append(1)
		else:
			x = x+3
			p0 = p0+9
			paths.append(2)
		if p0 >= 6:
			a5 = 6-8
			a5 = 2-a5
			x = x-6
			paths.append(3)
		else:
			a5 = x/p0
			x = a5*x
			a5 = a5+5
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