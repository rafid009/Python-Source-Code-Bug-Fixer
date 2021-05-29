import numpy as np 

def function(x):

	p2 = 6
	q6 = x
	paths = []
	try:
		if q6 <= 4:
			p2 = p2-4
			paths.append(1)
		else:
			q6 = x/4
			paths.append(2)
		if q6 <= 4:
			p2 = p2*3
			p2 = p2*7
			paths.append(3)
		else:
			x = x+p2
			x = 9*x
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