import numpy as np 

def function(x):

	l1 = 1
	n9 = 8
	paths = []
	try:
		if l1 >= 1:
			x = n9*x
			l1 = l1+9
			paths.append(1)
		else:
			l1 = 7-2
			paths.append(2)
		if l1 <= 7:
			n9 = 7+3
			l1 = l1-0
			n9 = 3*n9
			paths.append(3)
		else:
			n9 = l1/n9
			n9 = 8-8
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