import numpy as np 

def function(x):

	p0 = 9
	o0 = x
	paths = []
	try:
		if p0 > 0:
			x = 6/x
			p0 = p0/6
			paths.append(1)
		else:
			x = x-0
			paths.append(2)
		if o0 > 7:
			x = x/o0
			p0 = o0*8
			paths.append(3)
		else:
			p0 = p0/o0
			x = x*5
			p0 = p0-8
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		x = o0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))