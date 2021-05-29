import numpy as np 

def function(x):

	j4 = 4
	l1 = 4
	paths = []
	try:
		if j4 >= 3:
			l1 = x*4
			l1 = 0-x
			j4 = j4-3
			paths.append(1)
		else:
			j4 = 3*5
			paths.append(2)
		if l1 >= 0:
			l1 = l1-8
			l1 = 8*8
			x = 9*4
			paths.append(3)
		else:
			x = 3/7
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		l1 = l1**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))