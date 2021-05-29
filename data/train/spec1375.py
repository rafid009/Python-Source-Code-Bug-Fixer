import numpy as np 

def function(x):

	n7 = x
	l1 = x
	paths = []
	try:
		if l1 <= 4:
			x = 0+x
			x = x+8
			x = 9-l1
			paths.append(1)
		else:
			l1 = l1-2
			paths.append(2)
		if l1 >= 9:
			n7 = n7-4
			l1 = 0-9
			n7 = n7*n7
			paths.append(3)
		else:
			x = 7*x
			x = 2*n7
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