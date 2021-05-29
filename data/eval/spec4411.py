import numpy as np 

def function(x):

	p2 = x
	a7 = x
	x = 3
	paths = []
	try:
		if a7 > 4:
			p2 = x*p2
			a7 = p2-9
			a7 = x/p2
			paths.append(1)
		else:
			a7 = 6-3
			p2 = a7*p2
			x = 0*8
			paths.append(2)
		if p2 < 1:
			p2 = 1-a7
			x = p2-3
			x = 4*p2
			paths.append(3)
		else:
			p2 = a7+a7
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