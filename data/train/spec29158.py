import numpy as np 

def function(x):

	l9 = x
	n0 = 6
	paths = []
	try:
		if x > 9:
			l9 = l9*1
			paths.append(1)
		else:
			x = 6-7
			paths.append(2)
		if x > 0:
			n0 = 6*4
			n0 = n0+8
			x = 1*x
			paths.append(3)
		else:
			l9 = l9-x
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		l9 = l9**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))