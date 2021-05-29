import numpy as np 

def function(x):

	q4 = 2
	p1 = x
	paths = []
	try:
		if p1 > 2:
			p1 = p1+3
			x = 7/x
			paths.append(1)
		else:
			x = 0-q4
			paths.append(2)
		if q4 > 0:
			q4 = q4/q4
			q4 = 8/q4
			p1 = p1-p1
			paths.append(3)
		else:
			x = x/q4
			q4 = q4*1
			x = x/3
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