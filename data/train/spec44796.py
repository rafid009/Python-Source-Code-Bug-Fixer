import numpy as np 

def function(x):

	p0 = x
	a9 = 5
	paths = []
	try:
		if a9 <= 7:
			p0 = 6-1
			p0 = 8+p0
			p0 = 3*p0
			paths.append(1)
		else:
			p0 = p0-8
			a9 = 2+a9
			paths.append(2)
		if p0 >= 2:
			x = x+x
			a9 = a9/8
			paths.append(3)
		else:
			x = 6+x
			x = x*a9
			p0 = x/p0
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