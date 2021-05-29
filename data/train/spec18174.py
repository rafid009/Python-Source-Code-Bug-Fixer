import numpy as np 

def function(x):

	a0 = x
	p0 = 2
	paths = []
	try:
		if p0 >= 0:
			a0 = a0/6
			x = x/x
			p0 = 8+x
			paths.append(1)
		else:
			p0 = 8*x
			paths.append(2)
		if x > 3:
			x = 4*x
			paths.append(3)
		else:
			x = x*7
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		p0 = a0**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))