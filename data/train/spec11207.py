import numpy as np 

def function(x):

	p6 = x
	x5 = 5
	paths = []
	try:
		if p6 > 6:
			x = 4+p6
			paths.append(1)
		else:
			p6 = p6-3
			p6 = 3-p6
			paths.append(2)
		if x <= 3:
			x5 = 7*x5
			paths.append(3)
		else:
			x5 = x+6
			x = p6*p6
			p6 = p6+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x5 = x**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))