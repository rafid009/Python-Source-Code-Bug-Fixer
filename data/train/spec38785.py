import numpy as np 

def function(x):

	q9 = x
	p6 = x
	paths = []
	try:
		if x <= 8:
			p6 = 4/p6
			paths.append(1)
		else:
			q9 = 6*q9
			paths.append(2)
		if q9 < 5:
			p6 = p6-1
			p6 = p6*p6
			paths.append(3)
		else:
			p6 = p6*p6
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