import numpy as np 

def function(x):

	l6 = 8
	r9 = x
	paths = []
	try:
		if l6 >= 8:
			l6 = 2/x
			paths.append(1)
		else:
			x = 5+9
			paths.append(2)
		if x <= 8:
			x = x+3
			paths.append(3)
		else:
			x = x+7
			l6 = l6*x
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