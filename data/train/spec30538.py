import numpy as np 

def function(x):

	p0 = 2
	a6 = x
	paths = []
	try:
		if p0 < 9:
			p0 = 1/p0
			paths.append(1)
		else:
			p0 = 5-1
			p0 = p0*x
			paths.append(2)
		if a6 >= 8:
			x = 7+x
			paths.append(3)
		else:
			x = a6+x
			a6 = a6/9
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		p0 = a6**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))