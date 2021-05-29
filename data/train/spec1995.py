import numpy as np 

def function(x):

	p3 = x
	q9 = 1
	paths = []
	try:
		if q9 <= 3:
			q9 = x/x
			paths.append(1)
		else:
			p3 = 2+p3
			paths.append(2)
		if q9 >= 5:
			p3 = q9-3
			q9 = 2+5
			p3 = q9*p3
			paths.append(3)
		else:
			q9 = 5+3
			p3 = p3-0
			q9 = 9*q9
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