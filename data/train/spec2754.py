import numpy as np 

def function(x):

	l7 = 5
	x8 = x
	paths = []
	try:
		if x8 <= 8:
			l7 = l7/l7
			paths.append(1)
		else:
			x8 = x8+x8
			x8 = l7+x8
			paths.append(2)
		if x > 6:
			x = x-5
			paths.append(3)
		else:
			l7 = 4/x8
			l7 = 2+x
			l7 = 5*l7
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		x = l7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))