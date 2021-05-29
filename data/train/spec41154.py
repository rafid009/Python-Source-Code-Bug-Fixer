import numpy as np 

def function(x):

	l6 = 6
	p6 = 8
	paths = []
	try:
		if p6 <= 6:
			l6 = l6-6
			l6 = p6+l6
			paths.append(1)
		else:
			p6 = p6/6
			paths.append(2)
		if p6 > 7:
			x = x*x
			x = x+p6
			l6 = 9+l6
			paths.append(3)
		else:
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))