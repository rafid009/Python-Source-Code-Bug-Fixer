import numpy as np 

def function(x):

	p0 = 9
	r4 = 9
	paths = []
	try:
		if p0 >= 0:
			p0 = 7/4
			paths.append(1)
		else:
			r4 = p0-r4
			x = 4*2
			r4 = r4*p0
			paths.append(2)
		if p0 < 2:
			r4 = r4/3
			r4 = r4+x
			x = 6-x
			paths.append(3)
		else:
			p0 = p0/r4
			r4 = 5/x
			p0 = r4-1
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