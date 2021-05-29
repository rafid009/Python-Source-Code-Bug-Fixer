import numpy as np 

def function(x):

	e2 = 5
	p4 = x
	x = x
	paths = []
	try:
		if p4 > 8:
			e2 = e2+e2
			x = 4*4
			paths.append(1)
		else:
			e2 = x+e2
			x = 8*x
			p4 = p4*p4
			paths.append(2)
		if x > 9:
			x = x+7
			paths.append(3)
		else:
			x = 1*x
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p4 = x**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))