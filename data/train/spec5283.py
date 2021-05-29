import numpy as np 

def function(x):

	p9 = 6
	e5 = 9
	paths = []
	try:
		if e5 > 0:
			p9 = p9*5
			paths.append(1)
		else:
			x = 0/x
			paths.append(2)
		if x > 5:
			x = x*x
			paths.append(3)
		else:
			p9 = 4+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p9 = x**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))