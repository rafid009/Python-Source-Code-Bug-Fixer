import numpy as np 

def function(x):

	x6 = 3
	l7 = x
	paths = []
	try:
		if x6 >= 9:
			x = l7/x
			x6 = x6*l7
			paths.append(1)
		else:
			x = 6-3
			l7 = 1+l7
			x = 5+1
			paths.append(2)
		if x6 > 8:
			x = x/5
			l7 = 5/x
			paths.append(3)
		else:
			l7 = l7-x6
			x6 = 0-x6
			x6 = x6/x
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x6 = x6**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))