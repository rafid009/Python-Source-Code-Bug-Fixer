import numpy as np 

def function(x):

	p2 = 8
	q9 = x
	paths = []
	try:
		if p2 >= 1:
			q9 = q9+6
			paths.append(1)
		else:
			p2 = 3-p2
			x = p2+0
			x = q9*x
			paths.append(2)
		if q9 < 1:
			p2 = 6/p2
			x = q9/p2
			paths.append(3)
		else:
			q9 = x/p2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))