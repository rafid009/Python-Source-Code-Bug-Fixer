import numpy as np 

def function(x):

	q1 = x
	p6 = x
	paths = []
	try:
		if p6 > 0:
			q1 = q1+6
			x = x*6
			paths.append(1)
		else:
			q1 = x*q1
			paths.append(2)
		if q1 >= 1:
			q1 = q1/9
			x = x/7
			paths.append(3)
		else:
			p6 = 3+7
			x = 2/6
			q1 = q1/4
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