import numpy as np 

def function(x):

	l1 = x
	l2 = x
	paths = []
	try:
		if x >= 6:
			l2 = l2-8
			l1 = x/l1
			paths.append(1)
		else:
			l1 = l1+4
			x = x*5
			l1 = l1*3
			paths.append(2)
		if l2 <= 2:
			l2 = l2-9
			l1 = l1-4
			paths.append(3)
		else:
			l2 = l2+2
			l1 = l1+8
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		l2 = l1**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))