import numpy as np 

def function(x):

	n5 = x
	l1 = 1
	paths = []
	try:
		if x <= 2:
			l1 = l1+6
			l1 = 1*2
			x = x+4
			paths.append(1)
		else:
			l1 = 4+1
			x = 5/6
			paths.append(2)
		if x > 1:
			l1 = 9*x
			paths.append(3)
		else:
			l1 = 1*6
			x = l1/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l1 = x**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))