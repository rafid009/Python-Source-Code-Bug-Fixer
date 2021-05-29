import numpy as np 

def function(x):

	p0 = 2
	r0 = x
	paths = []
	try:
		if p0 > 2:
			x = x/8
			p0 = 7-7
			r0 = r0*7
			paths.append(1)
		else:
			x = 4*x
			r0 = 5+x
			paths.append(2)
		if p0 < 2:
			x = x*0
			paths.append(3)
		else:
			p0 = r0/2
			x = x*3
			x = x-9
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