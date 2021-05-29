import numpy as np 

def function(x):

	p2 = 4
	r1 = x
	paths = []
	try:
		if x > 5:
			p2 = p2-5
			p2 = p2+r1
			paths.append(1)
		else:
			p2 = 4*p2
			p2 = 0*p2
			x = 1*r1
			paths.append(2)
		if r1 <= 6:
			p2 = p2-1
			p2 = 1/x
			paths.append(3)
		else:
			r1 = p2-x
			r1 = 4-r1
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