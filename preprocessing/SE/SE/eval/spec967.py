import numpy as np 

def function(x):

	p2 = 3
	q4 = 5
	paths = []
	try:
		if x > 0:
			q4 = 2*q4
			paths.append(1)
		else:
			p2 = p2+p2
			paths.append(2)
		if p2 > 2:
			q4 = 0*q4
			q4 = q4/1
			paths.append(3)
		else:
			q4 = 2-0
			q4 = 5/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))