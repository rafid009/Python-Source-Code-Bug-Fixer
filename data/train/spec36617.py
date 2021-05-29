import numpy as np 

def function(x):

	p6 = 0
	q7 = x
	paths = []
	try:
		if x < 3:
			x = x/q7
			p6 = p6*4
			p6 = 8*5
			paths.append(1)
		else:
			x = 3-x
			paths.append(2)
		if q7 >= 0:
			p6 = p6+q7
			q7 = q7-7
			x = x-2
			paths.append(3)
		else:
			q7 = p6*q7
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		x = q7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))