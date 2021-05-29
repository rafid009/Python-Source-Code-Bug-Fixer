import numpy as np 

def function(x):

	l6 = 4
	x7 = 1
	paths = []
	try:
		if l6 <= 7:
			x7 = x7+x
			x = x*5
			x = x*x
			paths.append(1)
		else:
			x = 4*x
			x7 = x7-2
			paths.append(2)
		if x <= 4:
			x = x/x7
			x7 = x7*x
			x7 = 5+x7
			paths.append(3)
		else:
			x7 = l6*x7
			x7 = x7/4
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		l6 = x7**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))