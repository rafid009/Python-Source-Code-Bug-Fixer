import numpy as np 

def function(x):

	l9 = 4
	r9 = x
	x = 9
	paths = []
	try:
		if x >= 9:
			r9 = r9-x
			x = l9+r9
			r9 = r9*2
			paths.append(1)
		else:
			x = x/3
			r9 = 2+r9
			paths.append(2)
		if l9 < 9:
			l9 = l9+3
			l9 = 1-r9
			l9 = l9-8
			paths.append(3)
		else:
			x = 6*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r9 = x**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))