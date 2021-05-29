import numpy as np 

def function(x):

	q1 = x
	p7 = x
	paths = []
	try:
		if q1 <= 2:
			p7 = 0+x
			p7 = p7-q1
			p7 = p7*q1
			paths.append(1)
		else:
			x = 8+8
			p7 = p7*2
			paths.append(2)
		if q1 > 2:
			x = x/5
			p7 = p7-p7
			q1 = p7+x
			paths.append(3)
		else:
			x = 7*x
			x = 7+x
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p7 = x**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))