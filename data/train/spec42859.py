import numpy as np 

def function(x):

	p1 = 1
	e4 = 2
	paths = []
	try:
		if p1 > 0:
			p1 = e4+p1
			e4 = p1*7
			paths.append(1)
		else:
			p1 = p1*9
			e4 = 1-p1
			paths.append(2)
		if e4 <= 4:
			x = 2/p1
			paths.append(3)
		else:
			p1 = p1/e4
			p1 = p1+p1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))