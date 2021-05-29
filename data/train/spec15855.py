import numpy as np 

def function(x):

	p2 = 1
	q9 = x
	paths = []
	try:
		if p2 > 9:
			x = 7/x
			paths.append(1)
		else:
			q9 = x+p2
			p2 = 3/9
			paths.append(2)
		if x >= 1:
			x = q9*q9
			p2 = q9/3
			q9 = q9-9
			paths.append(3)
		else:
			x = x*7
			q9 = 8+q9
			p2 = p2-2
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