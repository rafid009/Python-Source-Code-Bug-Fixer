import numpy as np 

def function(x):

	p1 = x
	a5 = 9
	paths = []
	try:
		if x >= 8:
			x = x-8
			paths.append(1)
		else:
			x = 1+x
			a5 = 1+8
			p1 = 0-9
			paths.append(2)
		if x <= 2:
			p1 = p1*a5
			paths.append(3)
		else:
			x = x+1
			x = p1+0
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