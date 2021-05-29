import numpy as np 

def function(x):

	p1 = x
	c6 = 8
	paths = []
	try:
		if c6 < 3:
			p1 = p1*p1
			p1 = p1*p1
			p1 = p1+p1
			paths.append(1)
		else:
			p1 = 6*p1
			paths.append(2)
		if c6 >= 8:
			p1 = p1*4
			p1 = x+3
			paths.append(3)
		else:
			x = x+1
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