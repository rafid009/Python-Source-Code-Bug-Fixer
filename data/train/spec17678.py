import numpy as np 

def function(x):

	l4 = 0
	x6 = 6
	paths = []
	try:
		if l4 <= 2:
			x = x*6
			x6 = 5/x6
			paths.append(1)
		else:
			l4 = l4-3
			l4 = x6-x
			paths.append(2)
		if x <= 8:
			l4 = l4/x
			x6 = x/x6
			l4 = l4/9
			paths.append(3)
		else:
			x = 1*x6
			x6 = x6/x6
			x6 = 2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))