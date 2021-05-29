import numpy as np 

def function(x):

	a6 = 0
	p1 = x
	paths = []
	try:
		if a6 < 9:
			x = 4/x
			x = 8/x
			paths.append(1)
		else:
			a6 = a6+a6
			p1 = 2-0
			paths.append(2)
		if p1 > 9:
			a6 = a6-7
			paths.append(3)
		else:
			x = x+7
			p1 = p1-x
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