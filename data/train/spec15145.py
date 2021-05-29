import numpy as np 

def function(x):

	r9 = 2
	p2 = 1
	paths = []
	try:
		if p2 >= 8:
			x = x-8
			paths.append(1)
		else:
			r9 = 5*r9
			paths.append(2)
		if p2 >= 3:
			r9 = r9*p2
			p2 = x+r9
			paths.append(3)
		else:
			p2 = 7+3
			p2 = p2-r9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))