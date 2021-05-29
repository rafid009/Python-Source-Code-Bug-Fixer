import numpy as np 

def function(x):

	u0 = 1
	l7 = x
	paths = []
	try:
		if u0 < 0:
			u0 = 8*u0
			l7 = l7*4
			paths.append(1)
		else:
			x = x-3
			u0 = 1-8
			paths.append(2)
		if x > 7:
			l7 = 6+7
			x = 2*l7
			paths.append(3)
		else:
			u0 = 3*u0
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		l7 = l7**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))