import numpy as np 

def function(x):

	l1 = 2
	r5 = x
	x = x
	paths = []
	try:
		if x < 9:
			r5 = 9+r5
			paths.append(1)
		else:
			l1 = 8-0
			l1 = l1*r5
			paths.append(2)
		if x <= 0:
			x = x/4
			paths.append(3)
		else:
			l1 = l1/l1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))