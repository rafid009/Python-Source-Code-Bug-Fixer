import numpy as np 

def function(x):

	p0 = x
	d1 = 9
	paths = []
	try:
		if p0 < 4:
			p0 = p0-2
			p0 = d1*3
			d1 = 4-1
			paths.append(1)
		else:
			p0 = p0-2
			d1 = d1-2
			paths.append(2)
		if x < 5:
			p0 = x*p0
			p0 = 9+d1
			paths.append(3)
		else:
			d1 = d1-p0
			p0 = 2+x
			d1 = 9-d1
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