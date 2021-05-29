import numpy as np 

def function(x):

	r2 = x
	p0 = 0
	paths = []
	try:
		if r2 >= 7:
			r2 = 0-r2
			r2 = 5*p0
			paths.append(1)
		else:
			p0 = p0-8
			r2 = x-9
			paths.append(2)
		if r2 >= 7:
			x = x*p0
			paths.append(3)
		else:
			x = x/4
			x = 0/x
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