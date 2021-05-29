import numpy as np 

def function(x):

	l7 = x
	r9 = 4
	paths = []
	try:
		if l7 > 8:
			l7 = 5*9
			l7 = l7-6
			paths.append(1)
		else:
			x = 9/7
			r9 = 5+r9
			r9 = r9+l7
			paths.append(2)
		if r9 > 8:
			l7 = x/r9
			paths.append(3)
		else:
			l7 = l7/9
			x = l7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l7 = x**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))