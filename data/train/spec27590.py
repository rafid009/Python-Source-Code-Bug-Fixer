import numpy as np 

def function(x):

	l6 = 0
	l1 = 0
	paths = []
	try:
		if l6 < 2:
			l6 = 9*8
			x = x+8
			paths.append(1)
		else:
			x = 2-x
			l1 = 5/1
			l6 = x-6
			paths.append(2)
		if x < 0:
			l6 = 8-l6
			l1 = 6-l1
			l1 = 7/4
			paths.append(3)
		else:
			l6 = x+l1
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		l1 = l6**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))