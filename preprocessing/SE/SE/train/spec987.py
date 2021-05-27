import numpy as np 

def function(x):

	e7 = x
	p4 = x
	paths = []
	try:
		if e7 > 1:
			x = 7*x
			paths.append(1)
		else:
			e7 = 3+e7
			p4 = 0+p4
			paths.append(2)
		if x <= 9:
			x = e7+2
			e7 = 5-e7
			paths.append(3)
		else:
			p4 = p4+8
			x = 1+x
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