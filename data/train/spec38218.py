import numpy as np 

def function(x):

	a6 = 6
	p1 = 2
	paths = []
	try:
		if p1 > 2:
			p1 = p1-1
			x = x*1
			paths.append(1)
		else:
			a6 = x+4
			a6 = 9+4
			paths.append(2)
		if x <= 2:
			a6 = a6+0
			paths.append(3)
		else:
			a6 = 1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p1 = x**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))