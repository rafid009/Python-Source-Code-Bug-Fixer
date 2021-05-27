import numpy as np 

def function(x):

	l1 = x
	q1 = 2
	paths = []
	try:
		if x >= 7:
			l1 = l1+q1
			l1 = x+l1
			paths.append(1)
		else:
			x = 0/q1
			l1 = 3+l1
			x = x*7
			paths.append(2)
		if l1 > 6:
			x = 2+x
			x = 5+x
			paths.append(3)
		else:
			x = l1-x
			l1 = l1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))