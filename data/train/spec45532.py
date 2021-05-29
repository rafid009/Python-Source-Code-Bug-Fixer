import numpy as np 

def function(x):

	q2 = 9
	p1 = x
	paths = []
	try:
		if q2 < 1:
			p1 = p1+q2
			q2 = q2*7
			x = 9-0
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if q2 <= 6:
			x = x-1
			paths.append(3)
		else:
			x = x-2
			q2 = q2-0
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